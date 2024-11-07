use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["Found in the Infinitesimal Universe."];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"the infinitesimal universe",
			"a serial experience",
			"attack my voracity",
        ],
		unicode: true,
		padding: Padding::WordsInText,
		dotall: false,
		exceptions: &[],
	},
	path: "malapropisms.misc",
	msg: "'{}' is a malapropism.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
