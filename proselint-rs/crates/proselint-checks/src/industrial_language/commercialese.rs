use proselint_registry::checks::{Check, types::*, Padding};
use phf::phf_map;

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &[
	"We regret to inform you of this.",
	"The C.i.F. is free.",
];

const CHECK: Check = Check {
	check_type: &Existence {
		items: &[
			"acknowledging yours of",
			"beg to advise",
			"enclosed herewith",
			"enclosed please find",
			"further to yours of",
			"further to your letter",
			"in regard to",
			"in the amount of",
			"of even date",
			"pending receipt of",
			"please be advised that",
			"please return same",
			"pleasure of a reply",
			"pursuant to your request",
			"regarding the matter",
			"regret to inform",
			"thanking you in advance",
			"the undersigned",
			"this acknowledges your letter",
			"we are pleased to note",
			"with regard to",
			"your favor has come to hand",
			"yours of even date",
		],
		padding: Padding::WordsInText,
		exceptions: &[],
	},
	path: "industrial_language.commercialese",
	msg: "'{}' is commercialese.",
	..Check::default()
};

const CHECK_ABBREV: Check = Check {
	check_type: &PreferredForms {
		items: &phf_map!(
			r"inst\." => "this month",
			r"prox\." => "next month",
			r"ult\." => "last month",
			r"c\.i\.f\." => "cost, insurance, freight",
			r"f\.o\.b\." => "Free On Board",
		),
		padding: Padding::SeparatorInText,
	},
	path: "industrial_language.commercialese.abbreviations",
	msg: "'{1}' is commercialese. Depending on audience switch to {0}.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK, CHECK_ABBREV];
