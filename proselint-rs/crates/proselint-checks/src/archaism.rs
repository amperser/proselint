use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"I want to sleep, and maybe dream.",
];
pub const EXAMPLES_FAIL: &[&str] = &["I want to sleep, perchance to dream."];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"alack",
			"anent",
			// "anon",
			"begat",
			"belike",
			"betimes",
			"boughten",
			"brocage",
			"brokage",
			"camarade",
			"chiefer",
			"chiefest",
			"Christiana",
			"completely obsolescent",
			"cozen",
			"divers",
			"deflexion",
			"durst",
			"fain",
			"forsooth",
			"foreclose from",
			"haply",
			"howbeit",
			"illumine",
			"in sooth",
			"maugre",
			"meseems",
			"methinks",
			"nigh",
			"peradventure",
			"perchance",
			"saith",
			"shew",
			"sistren",
			"spake",
			"to wit",
			"verily",
			"whilom",
			"withal",
			"wot",
			"enclosed please find",
			"please find enclosed",
			"enclosed herewith",
			"enclosed herein",
			"inforce",
			"ex postfacto",
			"forewent",
			"for ever",
			// "designer", when used to mean a plotter against Christ
			// "demean", when used to mean "to behave" in legal contexts
			// "by the bye", # variant, modern is "by the by"
			// "comptroller" # in British English
			// "abortive" Abortive is archaic in reference to abortions,
			// except in the sense “causing an abortion.”
		],
		unicode: true,
		padding: Padding::WordsInText,
		dotall: false,
		exceptions: &[],
	},
	path: "archaism.misc",
	msg: "'{}' is archaic.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
