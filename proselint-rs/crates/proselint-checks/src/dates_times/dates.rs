use proselint_registry::{pad, checks::{Check, CheckType, Padding}};
use const_format::concatcp;

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"It happened in the 90s.",
	"It happened in the 1980s.",
	"It happened from 2000 to 2005.",
	"It happened in August 2008.",
	"It happened in August 2008.",
	"Dr. Dre suggested to 50's manager that he look into signing \
	Eminem to the G-Unit record label.",
];
pub const EXAMPLES_FAIL: &[&str] = &[
	"It happened in the 90's.",
	"It happened in the 1980's.",
	"It happened from 2000-2005.",
	"It happened in August, 2008.",
	"It happened in August of 2008.",
	"The 50's were swell.",
	"From 1999-2002, Sally served as chair of the committee.",
];

const CHECK_DECADES_APOSTROPHES_SHORT: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, r"\d0\'s"),
		exceptions: &[],
	},
	path: "dates_times.dates.apostrophes",
	msg: "Apostrophes aren't needed for decades.",
	..Check::default()
};

const CHECK_DECADES_APOSTROPHES_LONG: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, r"\d\d\d0\'s"),
		exceptions: &[],
	},
	path: "dates_times.dates.apostrophes",
	msg: "Apostrophes aren't needed for decades.",
	..Check::default()
};

const CHECK_DASH_AND_FROM: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(Padding::WordsInText, r"from \d+[^ \t\n\r\f\v\w.]\d+"),
		exceptions: &[],
	},
	path: "dates_times.dates.dash_and_from",
	msg: "When specifying a date range, write 'from X to Y'.",
	..Check::default()
};

// the Rust standard library does not have a list of months, nor a way to join
// instead of concat slices in a const context.
const MONTHS_SEPARATED: &str =
	"January|February|March|April|May|June|July \
	|August|September|October|November|December";

const CHECK_MONTH_YEAR_COMMA: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: concatcp!(pad!(Padding::SafeJoin, MONTHS_SEPARATED), r", \d{3,}"),
		exceptions: &[],
	},
	path: "dates_times.dates.month_year_comma",
	msg: "When specifying a month and year, no comma is needed.",
	..Check::default()
};

const CHECK_MONTH_OF_YEAR: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: concatcp!(pad!(Padding::SafeJoin, MONTHS_SEPARATED), r"of \d{3,}"),
		exceptions: &[],
	},
	path: "dates_times.dates.month_of_year",
	msg: "When specifying a month and year, 'of' is unnecessary.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[
	CHECK_DECADES_APOSTROPHES_SHORT,
	CHECK_DECADES_APOSTROPHES_LONG,
	CHECK_DASH_AND_FROM,
	CHECK_MONTH_YEAR_COMMA,
	CHECK_MONTH_OF_YEAR,
];
