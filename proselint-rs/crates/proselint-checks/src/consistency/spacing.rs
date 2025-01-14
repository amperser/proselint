use proselint_registry::checks::{Check, CheckType};

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"This is good. Only one space each time. Every time.",
];
pub const EXAMPLES_FAIL: &[&str] = &["This is bad.	Not consistent. At all."];

const CHECK: Check = Check {
	check_type: CheckType::Consistency {
		word_pairs: &[[r"[\.\?!] [A-Z]", r"[\.\?!]	[A-Z]"]]
	},
	path: "consistency.spacing",
	msg: "Inconsistent spacing after period (1 vs. 2 spaces).",
	ignore_case: false,
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
