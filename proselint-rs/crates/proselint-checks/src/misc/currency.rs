use proselint_registry::{pad, checks::{Check, types::*, Padding}};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["It cost $10 dollars."];

const CHECK: Check = Check {
	check_type: &ExistenceSimple {
		pattern: pad!(
			Padding::SeparatorInText,
			r"\$[\d]* ?(?:dollars|usd|us dollars)"
		),
		exceptions: &[],
	},
	path: "misc.currency",
	msg: "Incorrect use of symbols in {}.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
