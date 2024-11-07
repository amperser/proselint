use proselint_registry::{pad, checks::{Check, CheckType, Padding}};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["To say more research is needed."];

const CHECK: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, "more research is needed"),
		unicode: true,
		exceptions: &[],
	},
	path: "misc.apologizing",
	msg: "Excessive apologizing.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
