use const_format::str_replace;

use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &[
    "Smoke phrase with nothing flagged.",
    "It happened at 7 a.m.",
    "On Wed, Sep 21, 2016 at 11:42 AM -0400, X wrote:",
    "It happened at 7 a.m.",
    "It happened at noon.",
    "It happened at 7 a.m.",
];
pub const EXAMPLES_FAIL: &[&str] = &[
    "It happened at 7 am.",
    "It happened at 7a.m.",
    "It happened at 12 a.m.",
    "It happened at 12 p.m.",
    "It happened at 7a.m. in the morning.",
];

const CHECK_LOWERCASE_PERIODS: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: str_replace!(Padding::WordsInText.as_str(), "{}", r"\d{1,2} ?[ap]m"),
		unicode: true,
		exceptions: &[],
	},
	path: "dates_times.am_pm.lowercase_periods",
	msg: "With lowercase letters, periods are standard.",
	ignore_case: false,
	..Check::default()
};

const CHECK_SPACING: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: r"\b\d{1,2}[ap]\.?m\.?",
		unicode: true,
		exceptions: &[],
	},
	path: "dates_times.am_pm.spacing",
	msg: "It's standard to put a space before 'a.m.' or 'p.m.'.",
	..Check::default()
};

const CHECK_MIDNIGHT_NOON: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: r"\b12 ?[ap]\.?m\.?",
		unicode: true,
		exceptions: &[], 
	},
	path: "dates_times.am_pm.midnight_noon",
    msg: "12 a.m. and 12 p.m. are wrong and confusing. Use 'midnight' or 'noon'.",
	..Check::default()
};

const CHECK_REDUNDANCY: Check = Check {
	check_type: CheckType::Existence {
		items: &[
            r"\b\d{1,2} ?a\.?m\.? in the morning",
            r"\b\d{1,2} ?p\.?m\.? in the evening",
            r"\b\d{1,2} ?p\.?m\.? at night",
            r"\b\d{1,2} ?p\.?m\.? in the afternoon",
		],
		unicode: true,
		padding: Padding::None,
		dotall: false,
		exceptions: &[],
	},
	path: "dates_times.am_pm.redundancy",
	msg: "'a.m.' is always morning; 'p.m.' is always night.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[
	CHECK_LOWERCASE_PERIODS,
	CHECK_SPACING,
	CHECK_MIDNIGHT_NOON,
	CHECK_REDUNDANCY,
];
