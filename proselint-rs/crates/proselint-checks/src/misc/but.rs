use proselint_registry::{pad, checks::{Check, CheckType, Padding}};

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"I never start with the word \"but\", \
but might use it after a linebreak.",
	"Butter is the best.",
];
pub const EXAMPLES_FAIL: &[&str] = &[
	"But I never start with the word \"but\".",
	"But why are you like that.",
	"This is cool! But that not so much.",
	"Is this cool? But that not so much.",
];

const CHECK: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, r"(?:^|[\.!\?]\s*)But"),
		exceptions: &[],
	},
	path: "misc.but",
	msg: "No paragraph or sentence should start with a 'But'.",
	ignore_case: false,
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
