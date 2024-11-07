use proselint_registry::{pad, checks::{Check, CheckType, Padding}};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &[
	"I hope the report meets with your approval.",
];

const CHECK: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, r"(met|meets?) with your approval"),
		unicode: true,
		exceptions: &[],
	},
	path: "industrial_language.bureaucratese",
	msg: "'{}' is bureaucratese.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
