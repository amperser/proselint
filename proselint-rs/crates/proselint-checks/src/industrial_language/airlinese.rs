use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &[
    "Smoke phrase with nothing flagged.",
    "Did that car just hydroplane?",
    "I know how to operate a planing mill.",
];
pub const EXAMPLES_FAIL: &[&str] = &[
    "This is your captain speaking. We will be taking off momentarily.",
    "We deplaned promptly after.",
];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"enplan(?:e|ed|ing|ement)",
			"deplan(?:e|ed|ing|ement)",
			"taking off momentarily",
		],
		unicode: true,
		padding: Padding::WordsInText,
		dotall: false,
		exceptions: &[],
	},
	path: "industrial_language.airlinese",
	msg: "'{}' is airlinese.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
