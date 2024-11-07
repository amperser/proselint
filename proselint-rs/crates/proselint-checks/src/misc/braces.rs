use proselint_registry::checks::{Check, CheckType, CheckResult};
use regex::Regex;

pub const EXAMPLES_PASS: &[&str] = &[];
pub const EXAMPLES_FAIL: &[&str] = &[];

const BRACES: [(&str, (&str, &str)); 3] = [
	(r"[()]", ("(", ")")),
	(r"[{}]", ("{", "}")),
	(r"[\[\]]", ("[", "]"))
];

fn trace_braces(text: &str, pattern: &str, chars: (&str, &str), spec: &Check) -> Option<CheckResult> {
	let mut count: i8 = 0;
	for m in Regex::new(pattern).unwrap().find_iter(text) {
		count += (-1i8).pow((m.as_str() == chars.1) as u32);
		if count < 0 {
			return Some(CheckResult {
				start_pos: m.start(),
				end_pos: m.end(),
				check_name: spec.path.to_string(),
				message: format!("{} more '{}' were closed than opened.", spec.msg, chars.1),
				replacements: None,
			});
		}
	}
	(count > 0).then(|| CheckResult {
		start_pos: 0,
		end_pos: text.len(),
		check_name: spec.path.to_string(),
		message: format!("{} at least one '{}' is left open.", spec.msg, chars.0),
		replacements: None,
	})
}

fn check_unmatched(text: &str, spec: &Check) -> Vec<CheckResult> {
	BRACES
		.iter()
		.filter_map(|(pattern, chars)| trace_braces(text, pattern, *chars, spec))
		.collect()
}

const CHECK: Check = Check {
	check_type: CheckType::CheckFn(&check_unmatched),
	path: "misc.braces.unmatched",
	msg: "Match braces:",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
