use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["BRB getting coffee."];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"2day",
			"4U",
			"AFAIK",
			"AFK",
			"AFK",
			"ASAP",
			"B4",
			"brb",
			"btw",
			"cya",
			"GR8",
			"lol",
			"LUV",
			"OMG",
			"rofl",
			"rotfl",
			"sum1",
			"SWAK",
			"THNX",
			"THX",
			"TTYL",
			"XOXO",
		],
		unicode: true,
		padding: Padding::WordsInText,
		dotall: false,
		exceptions: &[],
	},
	path: "industrial_language.chatspeak",
	msg: "'{}' is chatspeak. Write it out.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
