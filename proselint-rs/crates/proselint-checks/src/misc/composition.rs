use proselint_registry::checks::{Check, CheckType, Padding};
use phf::phf_map;

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &[
	"His story is not honest.",
	"Her story is a strange one.",
	"He had not succeeded.",
	"He had not succeeded with that.",
];

const NAME: &str = "misc.composition";
const MSG: &str = "Try '{}' instead of '{}'.";

const CHECK: Check = Check {
	check_type: CheckType::PreferredFormsSimple {
		items: &phf_map!(
			// Put statements in positive form
			"not honest" => "dishonest",
			"not important" => "unimportant",
			"did not remember" => "forgot",
			"did not have much confidence in" => "distrusted",
			// Omit needless words
			"the question as to whether" => "whether",
			"there is no doubt but that" => "no doubt",
			"used for fuel purposes" => "used for fuel",
			"he is a man who" => "he",
			"in a hasty manner" => "hastily",
			"this is a subject that" => "this subject",
			"a strange one" => "strange",
			"the reason why is that" => "because",
			"owing to the fact that" => "because / since",
			"in spite of the fact that" => "although / though",
			"call your attention to the fact that" => "remind you / notify you",
			"was unaware of the fact that" => "did not know that / was unaware that",
			"not succeed" => "fail",
			"the fact that i had arrived" => "my arrival",
		),
		padding: Padding::WordsInText,
	},
	path: NAME,
	msg: MSG,
	..Check::default()
};

const CHECK_REGEX: Check = Check {
	check_type: CheckType::PreferredForms {
		items: &phf_map!(
			r"did not pay (any )?attention to" => "ignored",
			r"(had )?not succeeded" => "failed",
		),
		padding: Padding::WordsInText,
	},
	path: NAME,
	msg: MSG,
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK, CHECK_REGEX];
