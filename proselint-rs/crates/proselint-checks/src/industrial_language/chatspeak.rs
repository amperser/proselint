use proselint_registry::checks::{Check, types::*, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["BRB getting coffee."];

const CHECK: Check = Check {
	check_type: &Existence {
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
		padding: Padding::WordsInText,
		exceptions: &[],
	},
	path: "industrial_language.chatspeak",
	msg: "'{}' is chatspeak. Write it out.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
