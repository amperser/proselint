use proselint_registry::{pad, checks::{Check, types::*, Padding}};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &[
	"I hope the report meets with your approval.",
];

const CHECK: Check = Check {
	check_type: &ExistenceSimple {
		pattern: pad!(Padding::WordsInText, r"(met|meets?) with your approval"),
		exceptions: &[],
	},
	path: "industrial_language.bureaucratese",
	msg: "'{}' is bureaucratese.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
