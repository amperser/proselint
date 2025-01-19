use types::CheckType;

pub mod types;

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
	pub check_type: &'static dyn CheckType,
	pub path: &'static str,
	pub msg: &'static str,
	pub flags: CheckFlags,
	pub ignore_case: bool,
	pub offset: [usize; 2],
}

impl CheckType for Check {
	fn check(&self, text: &str, _: &Check) -> Vec<CheckResult> {
		self.check_type.check(text, self)
	}
}

fn default_check_fn(_: &str, _: &Check) -> Vec<CheckResult> {
	unimplemented!()
}

impl Check {
	pub const fn default() -> Self {
		Check {
			check_type: &default_check_fn,
			path: "",
			msg: "",
			flags: CheckFlags::default(),
			ignore_case: true,
			offset: [0, 0],
		}
	}
}
