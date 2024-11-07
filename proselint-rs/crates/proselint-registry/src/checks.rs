use fancy_regex::Regex;

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
}

#[macro_export]
macro_rules! pad {
	($padding:path, $text:expr$(,)?) => {
		const_format::str_replace!($padding.as_str(), "{}", $text)
	}
}

#[derive(Debug, Clone)]
pub struct LintResult {
	pub check_name: String,
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
	pub check_name: String,
	pub message: String,
	pub replacements: Option<String>,
}

#[derive(Clone, Copy)]
pub enum CheckType {
	Consistency {
		word_pairs: &'static [(&'static str, &'static str)],
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
		unicode: bool,
		padding: Padding,
		dotall: bool,
		exceptions: &'static [&'static str],
	},
	ExistenceSimple {
		pattern: &'static str,
		unicode: bool,
		exceptions: &'static [&'static str],
	},
	ReverseExistence {
		allowed: &'static [&'static str],
	},
	CheckFn(&'static dyn Fn(&str, &Check) -> Vec<CheckResult>),
}

impl CheckType {
	fn consistency(
		text: &str,
		word_pairs: &[(&str, &str)],
		path: &str,
		msg: &str,
		offset: (usize, usize),
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let mut results: Vec<CheckResult> = vec![];

		// NOTE: would it be more efficient to use a RegexSet and see which
		// pairs have matches for both, to prevent running multiple state
		// machines over the entire input?
		for word_pair in word_pairs {
			let matches: [Vec<fancy_regex::Match>; 2] = [
				Regex::new(word_pair.0)
					.unwrap()
					.find_iter(text)
					.filter_map(|x| x.ok())
					.collect(),
				Regex::new(word_pair.1)
					.unwrap()
					.find_iter(text)
					.filter_map(|x| x.ok())
					.collect(),
			];

			if matches[0].len() > 0 && matches[1].len() > 0 {
				let idx_minority =
					(matches[0].len() > matches[1].len()) as usize;

				results.append(
					&mut matches[idx_minority]
						.iter()
						.map(|m| CheckResult {
							start_pos: m.start() + offset.0,
							end_pos: m.end() + offset.1,
							check_name: path.to_string(),
							message: "".to_string(),
							replacements: Some(word_pair.0.to_string()),
						})
						.collect(),
				)
			}
		}
		results
	}

	fn preferred_forms(
		text: &str,
		items: &phf::Map<&str, &str>,
		path: &str,
		msg: &str,
		offset: (usize, usize),
		padding: Padding,
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let offset = match padding {
			Padding::None | Padding::SafeJoin | Padding::WordsInText => offset,
			_ => (offset.0 + 1, offset.1.saturating_sub(1)),
		};

		items
			.entries()
			.flat_map(|(original, replacement)| {
				Regex::new(&padding.pad(original))
					.unwrap()
					.find_iter(text)
					.filter_map(|m| {
						m.map(|x| CheckResult {
							start_pos: x.start() + offset.0,
							end_pos: x.end() + offset.1,
							check_name: path.to_string(),
							message: msg.to_string(),
							replacements: Some(replacement.to_string()),
						})
						.ok()
					})
					.collect::<Vec<_>>()
			})
			.collect()
	}

	fn preferred_forms_simple(
		text: &str,
		items: &phf::Map<&str, &str>,
		path: &str,
		msg: &str,
		offset: (usize, usize),
		padding: Padding,
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let offset = match padding {
			Padding::None | Padding::SafeJoin | Padding::WordsInText => offset,
			_ => (offset.0 + 1, offset.1.saturating_sub(1)),
		};

		let rx = &padding.pad(
			&(if items.len() > 1 {
				Padding::SafeJoin.pad(
					&items.keys().map(|x| *x).collect::<Vec<_>>().join("|"),
				)
			} else {
				items.keys().next().unwrap().to_string()
			}),
		);

		Regex::new(rx)
			.unwrap()
			.find_iter(text)
			.filter_map(|m| {
				m.ok().and_then(|x| {
					let original = x.as_str().trim();
					let replacements =
						items.get(original).map(|entry| entry.to_string());

					Some(CheckResult {
						start_pos: x.start() + offset.0,
						end_pos: x.end() + offset.1,
						check_name: path.to_string(),
						message: msg.to_string(),
						replacements,
					})
				})
			})
			.collect()
	}

	fn existence(
		text: &str,
		items: &[&str],
		path: &str,
		msg: &str,
		offset: (usize, usize),
		padding: Padding,
		exceptions: &[&str],
		ignore_case: bool,
		unicode: bool,
		dotall: bool,
	) -> Vec<CheckResult> {
		let offset = match padding {
			Padding::None | Padding::SafeJoin | Padding::WordsInText => offset,
			_ => (offset.0 + 1, offset.1.saturating_sub(1)),
		};

		let rx = &padding.pad(
			&(if items.len() > 1 {
				Padding::SafeJoin.pad(&items.join("|"))
			} else {
				items.first().unwrap().to_string()
			}),
		);

		let regex_exceptions = exceptions
			.iter()
			.map(|exception| Regex::new(exception).unwrap())
			.collect::<Vec<_>>();

		let mut results: Vec<CheckResult> = vec![];
		for m in Regex::new(rx).unwrap().find_iter(text).filter_map(|x| x.ok())
		{
			let txt = m.as_str().trim();
			if regex_exceptions
				.iter()
				.any(|exception| exception.is_match(txt).unwrap())
			{
				continue;
			}
			results.push(CheckResult {
				start_pos: m.start() + offset.0,
				end_pos: m.end() + offset.1,
				check_name: path.to_string(),
				message: msg.to_string(),
				replacements: None,
			});
		}
		results
	}

	fn existence_simple(
		text: &str,
		pattern: &str,
		path: &str,
		msg: &str,
		exceptions: &[&str],
		ignore_case: bool,
		unicode: bool,
	) -> Vec<CheckResult> {
		// TODO: this should be a RegexBuilder with case_insensitive
		// held up by fancy-regex#132
		let regex_pattern = Regex::new(pattern).unwrap();
		let regex_exceptions = exceptions
			.iter()
			.map(|exception| Regex::new(exception).unwrap())
			.collect::<Vec<_>>();
		let mut results: Vec<CheckResult> = Vec::new();
		for m in regex_pattern.find_iter(text).filter_map(|x| x.ok()) {
			if regex_exceptions
				.iter()
				.any(|exception| exception.is_match(m.as_str()).unwrap())
			{
				continue;
			}
			results.push(CheckResult {
				start_pos: m.start(),
				end_pos: m.end(),
				check_name: path.to_string(),
				message: m.as_str().trim().to_string(),
				replacements: None,
			})
		}
		results
	}

	fn rev_existence(
		text: &str,
		allowed: &[&str],
		path: &str,
		msg: &str,
		offset: (usize, usize),
		ignore_case: bool,
	) -> Vec<CheckResult> {
		let tokenizer = Regex::new(r"\w[\w'-]+\w").unwrap();
		tokenizer
			.find_iter(text)
			.filter_map(|m| {
				m.ok().and_then(|x| {
					let txt = x.as_str();
					if !txt.chars().any(|c| c.is_ascii_digit())
						&& !allowed.contains(&txt)
					{
						Some(CheckResult {
							start_pos: x.start() + offset.0 + 1,
							end_pos: x.end() + offset.1,
							check_name: path.to_string(),
							message: msg.to_string(),
							replacements: None,
						})
					} else {
						None
					}
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
	// pub x: &'static dyn Fn(&'static [&'static str]) -> &str,
	pub flags: CheckFlags,
	pub ignore_case: bool,
	pub offset: (usize, usize),
}

impl Check {
	pub const fn default() -> Self {
		Check {
			check_type: CheckType::CheckFn(&|_, _| { vec![] }),
			path: "",
			msg: "",
			flags: CheckFlags::default(),
			ignore_case: true,
			offset: (0, 0),
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
			Existence { items, unicode, padding, dotall, exceptions } => {
				CheckType::existence(
					text,
					items,
					self.path,
					self.msg,
					self.offset,
					padding,
					exceptions,
					self.ignore_case,
					unicode,
					dotall,
				)
			}
			ExistenceSimple { pattern, unicode, exceptions } => {
				CheckType::existence_simple(
					text,
					pattern,
					self.path,
					self.msg,
					exceptions,
					self.ignore_case,
					unicode,
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
