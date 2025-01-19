use proselint_registry::{pad, checks::{Check, types::*, Padding}};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &[
	"We should preplan the trip.",
	"To coin a phrase from him, No diggity",
	"Not without your collusion you won't'.",
	"it fills a much-needed gap",
];

const CHECK: Check = Check {
	check_type: &Existence {
		items: &[
			"preplan",
			r"more than .{1,10} all",
			r"appraisal valuations?",
			r"(?:i|you|he|she|it|y'all|all y'all|you all|they) could care less",
			"least worst",
			r"much-needed gaps?",
			r"much-needed voids?",
			"no longer requires oxygen",
			"without scarcely",
		],
		padding: Padding::WordsInText,
		exceptions: &[],
	},
	path: "misc.illogic",
	msg: "'{}' is illogical.",
	..Check::default()
};

const CHECK_COIN: Check = Check {
	check_type: &ExistenceSimple {
		pattern: pad!(Padding::WordsInText, "to coin a phrase from"),
		exceptions: &[],
	},
	path: "misc.illogic.coin",
	msg: "You can't coin an existing phrase. Did you mean 'borrow'?",
	..Check::default()
};

const CHECK_COLLUSION: Check = Check {
	check_type: &ExistenceSimple {
		pattern: pad!(Padding::WordsInText, "without your collusion"),
		exceptions: &[],
	},
	path: "misc.illogic.collusion",
	msg: "It's impossible to defraud yourself. Try 'acquiescence'.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK, CHECK_COIN, CHECK_COLLUSION];
