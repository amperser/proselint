use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"Add it to the to-do list.",
];
pub const EXAMPLES_FAIL: &[&str] = &[
	"Add it to the TODO list.",
];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"FIXME",
			"FIX ME",
			"TODO",
			"todo",
			"ERASE THIS",
			"FIX THIS",
		],
		padding: Padding::WordsInText,
		exceptions: &[],
	},
	path: "annotations.misc",
	msg: "Annotation left in text.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
