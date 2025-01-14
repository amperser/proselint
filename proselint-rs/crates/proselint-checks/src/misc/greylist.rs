use proselint_registry::{pad, checks::{Check, CheckType, Padding}};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &[
	"She should utilize her knowledge.",
	"This is obviously an inadvisable word to use obviously.",
	"I utilize a hammer to drive nails into wood.",
	"Do you know anyone who *needs* to utilize the word utilize?",
];

const CHECK_OBVIOUSLY: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, "obviously"),
		exceptions: &[],
	},
	path: "misc.greylist.obviously",
	msg: "Use of 'obviously'. This is obviously an inadvisable word to use.",
	..Check::default()
};

const CHECK_UTILIZE: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, "utilize"),
		exceptions: &[],
	},
	path: "misc.greylist.utilize",
	msg: "Use of 'utilize'. \
	Do you know anyone who needs to utilize the word utilize?",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK_OBVIOUSLY, CHECK_UTILIZE];
