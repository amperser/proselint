use phf::phf_map;
use regex::{Match, Regex, RegexBuilder};

use super::{Check, CheckResult, Padding};

pub trait CheckFn: Fn(&str, &Check) -> Vec<CheckResult> + Send + Sync {}

impl<T: Fn(&str, &Check) -> Vec<CheckResult> + Send + Sync> CheckFn for T {}

pub trait CheckType {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult>;
}

impl<T: CheckFn> CheckType for T {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult> {
		self(text, check)
	}
}

pub struct Consistency {
	pub word_pairs: &'static [[&'static str; 2]],
}

impl Consistency {
	pub const fn default() -> Self {
		Consistency { word_pairs: &[] }
	}
}

impl CheckType for Consistency {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult> {
		let mut results: Vec<CheckResult> = vec![];

		for pair in self.word_pairs {
			let matches: [Vec<Match>; 2] = pair
				.iter()
				.map(|part| {
					RegexBuilder::new(part)
						.case_insensitive(check.ignore_case)
						.build()
						.unwrap()
						.find_iter(text)
						.collect::<Vec<_>>()
				})
				.collect::<Vec<_>>()
				.try_into()
				.unwrap();

			let idx_minority = (matches[0].len() > matches[1].len()) as usize;
			results.extend(matches[idx_minority].iter().map(|m| {
				CheckResult {
					start_pos: m.start() + check.offset[0],
					end_pos: m.end() + check.offset[1],
					check_name: check.path,
					message: check.msg.to_string(),
					replacements: Some(pair[0].to_string()),
				}
			}));
		}
		results
	}
}

pub struct PreferredForms {
	pub items: &'static phf::Map<&'static str, &'static str>,
	pub padding: Padding,
}

impl PreferredForms {
	pub const fn default() -> Self {
		PreferredForms { items: &phf_map! {}, padding: Padding::WordsInText }
	}
}

impl CheckType for PreferredForms {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult> {
		let offset = self.padding.to_offset_from(check.offset);

		// TODO: benchmark replacing this with RegexSet
		self.items
			.entries()
			.flat_map(|(original, replacement)| {
				RegexBuilder::new(&self.padding.pad(original))
					.case_insensitive(check.ignore_case)
					.build()
					.unwrap()
					.find_iter(text)
					.map(|m| CheckResult {
						start_pos: m.start() + offset[0],
						end_pos: m.end() + offset[1],
						check_name: check.path,
						message: check.msg.to_string(),
						replacements: Some(replacement.to_string()),
					})
					.collect::<Vec<_>>()
			})
			.collect()
	}
}

pub struct PreferredFormsSimple {
	pub items: &'static phf::Map<&'static str, &'static str>,
	pub padding: Padding,
}

impl PreferredFormsSimple {
	pub const fn default() -> Self {
		PreferredFormsSimple {
			items: &phf_map! {},
			padding: Padding::WordsInText,
		}
	}
}

impl CheckType for PreferredFormsSimple {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult> {
		let offset = self.padding.to_offset_from(check.offset);

		let rx = &self.padding.pad(
			&(if self.items.len() > 1 {
				Padding::SafeJoin.pad(
					&self.items.keys().copied().collect::<Vec<_>>().join("|"),
				)
			} else {
				self.items.keys().next().unwrap().to_string()
			}),
		);

		// TODO: benchmark replacing this with RegexSet
		RegexBuilder::new(rx)
			.case_insensitive(check.ignore_case)
			.build()
			.unwrap()
			.find_iter(text)
			.map(|m| {
				let original = m.as_str().trim();
				let replacements =
					self.items.get(original).map(|entry| entry.to_string());

				CheckResult {
					start_pos: m.start() + offset[0],
					end_pos: m.end() + offset[1],
					check_name: check.path,
					message: check.msg.to_string(),
					replacements,
				}
			})
			.collect()
	}
}

pub struct Existence {
	pub items: &'static [&'static str],
	pub padding: Padding,
	pub exceptions: &'static [&'static str],
}

impl Existence {
	pub const fn default() -> Self {
		Existence {
			items: &[],
			padding: Padding::WordsInText,
			exceptions: &[],
		}
	}
}

impl CheckType for Existence {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult> {
		let offset = self.padding.to_offset_from(check.offset);

		let rx = &self.padding.pad(
			&(if self.items.len() > 1 {
				Padding::SafeJoin.pad(&self.items.join("|"))
			} else {
				self.items.first().unwrap().to_string()
			}),
		);

		let regex_exceptions = self
			.exceptions
			.iter()
			.map(|exception| {
				RegexBuilder::new(exception)
					.case_insensitive(check.ignore_case)
					.build()
					.unwrap()
			})
			.collect::<Vec<_>>();

		regex::RegexBuilder::new(rx)
			.case_insensitive(check.ignore_case)
			.build()
			.unwrap()
			.find_iter(text)
			.filter_map(|m| {
				let match_text = m.as_str().trim();
				(!regex_exceptions
					.iter()
					.any(|exception| exception.is_match(match_text)))
				.then(|| CheckResult {
					start_pos: m.start() + offset[0],
					end_pos: m.end() + offset[1],
					check_name: check.path,
					message: check.msg.to_string(),
					replacements: None,
				})
			})
			.collect()
	}
}

pub struct ExistenceSimple {
	pub pattern: &'static str,
	pub exceptions: &'static [&'static str],
}

impl ExistenceSimple {
	pub const fn default() -> Self {
		ExistenceSimple { pattern: "", exceptions: &[] }
	}
}

impl CheckType for ExistenceSimple {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult> {
		// TODO: this should be a RegexBuilder with case_insensitive
		// held up by fancy-regex#132
		let regex_pattern = fancy_regex::Regex::new(self.pattern).unwrap();
		let regex_exceptions = self
			.exceptions
			.iter()
			.map(|exception| fancy_regex::Regex::new(exception).unwrap())
			.collect::<Vec<_>>();
		regex_pattern
			.find_iter(text)
			.filter_map(|x| {
				x.ok().and_then(|m| {
					(!regex_exceptions.iter().any(|exception| {
						exception.is_match(m.as_str()).unwrap()
					}))
					.then(|| CheckResult {
						start_pos: m.start(),
						end_pos: m.end(),
						check_name: check.path,
						message: check.msg.to_string(),
						replacements: None,
					})
				})
			})
			.collect()
	}
}

pub struct ReverseExistence {
	pub allowed: &'static [&'static str],
}

impl ReverseExistence {
	pub const fn default() -> Self {
		ReverseExistence { allowed: &[] }
	}
}

impl CheckType for ReverseExistence {
	fn check(&self, text: &str, check: &Check) -> Vec<CheckResult> {
		let tokenizer = Regex::new(r"\w[\w'-]+\w").unwrap();
		tokenizer
			.find_iter(text)
			.filter_map(|m| {
				let match_text = m.as_str();
				(!match_text.chars().any(|c| c.is_ascii_digit())
					&& !self.allowed.contains(&match_text))
				.then(|| CheckResult {
					start_pos: m.start() + check.offset[0] + 1,
					end_pos: m.end() + check.offset[1],
					check_name: check.path,
					message: check.msg.to_string(),
					replacements: None,
				})
			})
			.collect()
	}
}
