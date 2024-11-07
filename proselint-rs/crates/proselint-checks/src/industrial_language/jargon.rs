use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["I agree it's in the affirmative."];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"in the affirmative",
			"in the negative",
			"agendize",
			"per your order",
			"per your request",
			"disincentivize",
		],
		unicode: true,
		padding: Padding::WordsInText,
		dotall: false,
		exceptions: &[],
	},
	path: "industrial_language.jargon",
	msg: "'{}' is jargon. Can you replace it with something more standard?",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
