use proselint_registry::{pad, checks::{Check, CheckType, CheckResult, Padding}};
use phf::phf_map;

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"Smoke Stone Age with nothing flagged.",
	"Smoke winter with nothing flagged",
	"world war II",
	"XVII",
];
pub const EXAMPLES_FAIL: &[&str] = &[
	"It goes back to the stone age.",
	"A nice day during Winter.",
	"A nice day in Spring.",
	"A nice day in june.",
	"It happened on friday.",
	"World War ii",
	"World War i",
	"world War Ii", // not covered by war-check
	"MCVi",
	"CLx",
	"mCv",
];

const CHECK_TERMS: Check = Check {
	check_type: CheckType::PreferredFormsSimple {
		items: &phf_map!(
			"stone age" => "Stone Age",
			"Space Age" => "space age",
			"the American west" => "the American West",
			"mother nature" => "Mother Nature",
		),
		padding: Padding::WordsInText,
	},
	path: "misc.capitalization.terms",
	msg: "Incorrect capitalization. '{}' is the preferred form.",
	ignore_case: false,
	..Check::default()
};

const CHECK_SEASONS: Check = Check {
	check_type: CheckType::PreferredFormsSimple {
		items: &phf_map!(
			"Winter" => "winter",
			"Fall" => "fall",
			"Summer" => "summer",
			"Spring" => "spring",
		),
		padding: Padding::WordsInText,
	},
	path: "misc.capitalization.seasons",
	msg: "Seasons shouldn't be capitalized. '{}' is the preferred form.",
	ignore_case: false,
	..Check::default()
};

const CHECK_MONTHS: Check = Check {
	// too many false positives: may, march
	// TODO: deal with collisions
	//		 i.e. "(you|he|...) may proceed" follows a pattern
	check_type: CheckType::PreferredFormsSimple {
		items: &phf_map!(
			"january" => "January",
			"february" => "February",
			"april" => "April",
			"june" => "June",
			"july" => "July",
			"august" => "August",
			"september" => "September",
			"october" => "October",
			"november" => "November",
			"december" => "December",
		),
		padding: Padding::WordsInText,
	},
	path: "misc.capitalization.months",
	msg: "Months should be capitalized. '{}' is the preferred form.",
	ignore_case: false,
	..Check::default()
};

const CHECK_DAYS: Check = Check {
	check_type: CheckType::PreferredFormsSimple {
		items: &phf_map!(
			"monday" => "Monday",
			"tuesday" => "Tuesday",
			"wednesday" => "Wednesday",
			"thursday" => "Thursday",
			"friday" => "Friday",
			"saturday" => "Saturday",
			"sunday" => "Sunday",
		),
		padding: Padding::WordsInText,
	},
	path: "misc.capitalization.days",
	msg: "Days of the week should be capitalized. '{}' is the preferred form.",
	ignore_case: false,
	..Check::default()
};

const CHECK_ROMAN_WAR: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: r"World War ((I*i+)|(i+I*))+",
		exceptions: &[],
	},
	path: "misc.capitalization.roman_num.ww",
	msg: "Capitalize the roman numeral in '{}'.",
	ignore_case: false,
	..Check::default()
};

// TODO: this could be tidier if a filter flag existed
// it also should not be split into two checks - refactor if possible
const _CHECK_ROMAN_NUMERALS: Check = Check {
	check_type: CheckType::ExistenceSimple {
		pattern: pad!(
			Padding::WordsInText,
			r"M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})",
		),
		exceptions: &[],
	},
	path: "misc.capitalization.roman_num",
	msg: "Capitalize the roman numeral '{}'.",
	ignore_case: true,
	..Check::default()
};
const NUMERALS: [char; 7] = ['m', 'd', 'c', 'l', 'x', 'v', 'i'];

fn check_roman_numerals(text: &str, _check: &Check) -> Vec<CheckResult> {
	_CHECK_ROMAN_NUMERALS
		.dispatch(text)
		.into_iter()
		.filter(|result| {
			let item = text[result.start_pos..result.end_pos].trim();
			item.len() > 0 && item.chars().any(|x| NUMERALS.contains(&x))
		})
		.collect()
}

const CHECK_ROMAN_NUMERALS: Check = Check {
	check_type: CheckType::CheckFn(&check_roman_numerals),
	path: "misc.capitalization.roman_num",
	msg: "Capitalize the roman numeral '{}'.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[
	CHECK_TERMS,
	CHECK_SEASONS,
	CHECK_MONTHS,
	CHECK_DAYS,
	CHECK_ROMAN_WAR,
	CHECK_ROMAN_NUMERALS,
];
