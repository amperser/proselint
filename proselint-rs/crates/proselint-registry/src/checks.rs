use regex::{Match, Regex, RegexBuilder};

#[derive(Clone, Copy, Debug, Default)]
pub enum Padding {
	None,
	SafeJoin,
	Whitespace,
	SeparatorInText,
	#[default]
	WordsInText,
}

impl Padding {
	pub const fn as_str(&self) -> &str {
		match self {
			Padding::None => r"{}",
			Padding::SafeJoin => r"(?:{})",
			Padding::Whitespace => r"\s{}\s",
			Padding::SeparatorInText => r"(?:^|\W){}[\W$]",
			Padding::WordsInText => r"\b{}\b",
		}
	}

	/// Pad some `text` with the selected variant.
	///
	/// # Const padding
	///
	/// For padding at compile-time, use `pad!` instead.
	pub fn pad(&self, text: &str) -> String {
		self.as_str().replace(r"{}", text)
	}

	pub const fn to_offset_from(&self, offset: [usize; 2]) -> [usize; 2] {
		match self {
			Padding::None | Padding::SafeJoin | Padding::WordsInText => offset,
			_ => [offset[0] + 1, offset[1].saturating_sub(1)],
		}
	}
}

#[macro_export]
macro_rules! pad {
	($padding:path, $text:expr$(,)?) => {
		const_format::str_replace!($padding.as_str(), "{}", $text)
	};
}

#[derive(Debug, Clone)]
pub struct LintResult {
	pub check_name: &'static str,
	pub message: String,
	pub source: String,
	pub line: usize,
	pub column: usize,
	pub start: usize,
	pub end: usize,
	pub extent: usize,
	pub severity: String,
	pub replacements: Option<String>,
}

#[derive(Debug)]
pub struct CheckResult {
	pub start_pos: usize,
	pub end_pos: usize,
	pub check_name: &'static str,
	pub message: String,
	pub replacements: Option<String>,
}

pub trait CheckFn: Fn(&str, &Check) -> Vec<CheckResult> + Send + Sync {}

impl<T: Fn(&str, &Check) -> Vec<CheckResult> + Send + Sync> CheckFn for T {}

#[derive(Clone, Copy)]
pub enum CheckType {
	Consistency {
		word_pairs: &'static [[&'static str; 2]],
	},
	PreferredForms {
		items: &'static phf::Map<&'static str, &'static str>,
		padding: Padding,
	},
	PreferredFormsSimple {
		items: &'static phf::Map<&'static str, &'static str>,
		padding: Padding,
	},
	Existence {
		items: &'static [&'static str],
		padding: Padding,
		exceptions: &'static [&'static str],
	},
	ExistenceSimple {
		pattern: &'static str,
		exceptions: &'static [&'static str],
	},
	ReverseExistence {
		allowed: &'static [&'static str],
	},
	CheckFn(&'static dyn CheckFn),
}

impl CheckType {
	fn consistency(
		text: &str,
		word_pairs: &[[&str; 2]],
		path: &'static str,
		msg: &str,
		offset: [usize; 2],
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let mut results: Vec<CheckResult> = vec![];

		for pair in word_pairs {
			let matches: [Vec<Match>; 2] = pair
				.iter()
				.map(|part| {
					RegexBuilder::new(part)
						.case_insensitive(ignore_case)
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
					start_pos: m.start() + offset[0],
					end_pos: m.end() + offset[1],
					check_name: path,
					message: msg.to_string(),
					replacements: Some(pair[0].to_string()),
				}
			}));
		}
		results
	}

	fn preferred_forms(
		text: &str,
		items: &phf::Map<&str, &str>,
		path: &'static str,
		msg: &str,
		offset: [usize; 2],
		padding: Padding,
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let offset = padding.to_offset_from(offset);

		// TODO: benchmark replacing this with RegexSet
		items
			.entries()
			.flat_map(|(original, replacement)| {
				RegexBuilder::new(&padding.pad(original))
					.case_insensitive(ignore_case)
					.build()
					.unwrap()
					.find_iter(text)
					.map(|m| CheckResult {
						start_pos: m.start() + offset[0],
						end_pos: m.end() + offset[1],
						check_name: path,
						message: msg.to_string(),
						replacements: Some(replacement.to_string()),
					})
					.collect::<Vec<_>>()
			})
			.collect()
	}

	fn preferred_forms_simple(
		text: &str,
		items: &phf::Map<&str, &str>,
		path: &'static str,
		msg: &str,
		offset: [usize; 2],
		padding: Padding,
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let offset = padding.to_offset_from(offset);

		let rx = &padding.pad(
			&(if items.len() > 1 {
				Padding::SafeJoin.pad(
					&items.keys().map(|x| *x).collect::<Vec<_>>().join("|"),
				)
			} else {
				items.keys().next().unwrap().to_string()
			}),
		);

		// TODO: benchmark replacing this with RegexSet
		RegexBuilder::new(rx)
			.case_insensitive(ignore_case)
			.build()
			.unwrap()
			.find_iter(text)
			.map(|m| {
				let original = m.as_str().trim();
				let replacements =
					items.get(original).map(|entry| entry.to_string());

				CheckResult {
					start_pos: m.start() + offset[0],
					end_pos: m.end() + offset[1],
					check_name: path,
					message: msg.to_string(),
					replacements,
				}
			})
			.collect()
	}

	fn existence(
		text: &str,
		items: &[&str],
		path: &'static str,
		msg: &str,
		offset: [usize; 2],
		padding: Padding,
		exceptions: &[&str],
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let offset = padding.to_offset_from(offset);

		let rx = &padding.pad(
			&(if items.len() > 1 {
				Padding::SafeJoin.pad(&items.join("|"))
			} else {
				items.first().unwrap().to_string()
			}),
		);

		let regex_exceptions = exceptions
			.iter()
			.map(|exception| {
				RegexBuilder::new(exception)
					.case_insensitive(ignore_case)
					.build()
					.unwrap()
			})
			.collect::<Vec<_>>();

		regex::RegexBuilder::new(rx)
			.case_insensitive(ignore_case)
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
					check_name: path,
					message: msg.to_string(),
					replacements: None,
				})
			})
			.collect()
	}

	fn existence_simple(
		text: &str,
		pattern: &str,
		path: &'static str,
		msg: &str,
		exceptions: &[&str],
		ignore_case: bool,
	) -> Vec<CheckResult> {
		// TODO: this should be a RegexBuilder with case_insensitive
		// held up by fancy-regex#132
		let regex_pattern = fancy_regex::Regex::new(pattern).unwrap();
		let regex_exceptions = exceptions
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
						check_name: path,
						message: msg.to_string(),
						replacements: None,
					})
				})
			})
			.collect()
	}

	fn rev_existence(
		text: &str,
		allowed: &[&str],
		path: &'static str,
		msg: &str,
		offset: [usize; 2],
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let tokenizer = Regex::new(r"\w[\w'-]+\w").unwrap();
		tokenizer
			.find_iter(text)
			.filter_map(|m| {
				let match_text = m.as_str();
				(!match_text.chars().any(|c| c.is_ascii_digit())
					&& !allowed.contains(&match_text))
				.then(|| CheckResult {
					start_pos: m.start() + offset[0] + 1,
					end_pos: m.end() + offset[1],
					check_name: path,
					message: msg.to_string(),
					replacements: None,
				})
			})
			.collect()
	}
}

#[derive(Clone, Copy, Debug)]
pub struct CheckFlags {
	pub limit_results: u8,
	pub ppm_threshold: u32,
}

impl CheckFlags {
	const fn default() -> Self {
		CheckFlags { limit_results: 0, ppm_threshold: 0 }
	}
}

#[derive(Clone, Copy)]
pub struct Check {
	pub check_type: CheckType,
	pub path: &'static str,
	pub msg: &'static str,
	pub flags: CheckFlags,
	pub ignore_case: bool,
	pub offset: [usize; 2],
}

impl Check {
	pub const fn default() -> Self {
		Check {
			check_type: CheckType::CheckFn(&|_, _| vec![]),
			path: "",
			msg: "",
			flags: CheckFlags::default(),
			ignore_case: true,
			offset: [0, 0],
		}
	}

	pub fn dispatch(&self, text: &str) -> Vec<CheckResult> {
		use CheckType::*;

		match self.check_type.to_owned() {
			Consistency { word_pairs } => CheckType::consistency(
				text,
				word_pairs,
				self.path,
				self.msg,
				self.offset,
				self.ignore_case,
			),
			PreferredForms { items, padding } => CheckType::preferred_forms(
				text,
				items,
				self.path,
				self.msg,
				self.offset,
				padding,
				self.ignore_case,
			),
			PreferredFormsSimple { items, padding } => {
				CheckType::preferred_forms_simple(
					text,
					items,
					self.path,
					self.msg,
					self.offset,
					padding,
					self.ignore_case,
				)
			}
			Existence { items, padding, exceptions } => {
				CheckType::existence(
					text,
					items,
					self.path,
					self.msg,
					self.offset,
					padding,
					exceptions,
					self.ignore_case,
				)
			}
			ExistenceSimple { pattern, exceptions } => {
				CheckType::existence_simple(
					text,
					pattern,
					self.path,
					self.msg,
					exceptions,
					self.ignore_case,
				)
			}
			ReverseExistence { allowed } => CheckType::rev_existence(
				text,
				allowed,
				self.path,
				self.msg,
				self.offset,
				self.ignore_case,
			),
			CheckFn(check_fn) => check_fn(text, self),
		}
	}
}
