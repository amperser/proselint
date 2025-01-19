use proselint_registry::checks::{Check, types::*, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["Found in the Infinitesimal Universe."];

const CHECK: Check = Check {
	check_type: &Existence {
		items: &[
			"the infinitesimal universe",
			"a serial experience",
			"attack my voracity",
        ],
		padding: Padding::WordsInText,
		exceptions: &[],
	},
	path: "malapropisms.misc",
	msg: "'{}' is a malapropism.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
