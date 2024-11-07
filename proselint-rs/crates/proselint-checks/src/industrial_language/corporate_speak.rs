use proselint_registry::checks::{Check, CheckType, Padding};

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"We will discuss it later.",
];
pub const EXAMPLES_FAIL: &[&str] = &["We will circle back around to it."];

const CHECK: Check = Check {
	check_type: CheckType::Existence {
		items: &[
			"at the end of the day",
			"back to the drawing board",
			"hit the ground running",
			"get the ball rolling",
			"low-hanging fruit",
			"thrown under the bus",
			"think outside the box",
			"let's touch base",
			"get my manager's blessing",
			"it's on my radar",
			"ping me",
			"i don't have the bandwidth",
			"no brainer",
			"par for the course",
			"bang for your buck",
			"synergy",
			"move the goal post",
			"apples to apples",
			"win-win",
			"circle back around",
			"all hands on deck",
			"take this offline",
			"drill-down",
			"elephant in the room",
			"on my plate",
		],
		unicode: true,
		padding: Padding::WordsInText,
		dotall: false,
		exceptions: &[],
	},
	path: "industrial_language.corporate_speak",
	msg: "Minimize your use of corporate catchphrases like this one.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
