use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &[
    "I would argue that this is a good test.",
    "You could say that, so to speak.",
];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"I would argue that",
			"so to speak",
			"to a certain degree",
		],
		padding: Padding::WordsInText,
		exceptions: &[],
	},
	path: "hedging.misc",
	msg: "Hedging. Just say it.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
