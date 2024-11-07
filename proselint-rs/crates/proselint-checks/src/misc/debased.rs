use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["This leaves much to be desired."];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"a not unjustifiable assumption",
			"leaves much to be desired",
			"would serve no purpose",
			"a consideration which we should do well to bear in mind",
		],
		unicode: true,
		padding: Padding::WordsInText,
		dotall: false,
		exceptions: &[],
	},
	path: "misc.debased",
	msg: "Debased language is a continuous temptation.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
