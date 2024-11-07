use proselint_registry::checks::{Check, CheckType};

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"The centre for the arts is the art centre.",
	"The center for the arts is the art center.",
];
pub const EXAMPLES_FAIL: &[&str] = &[
	"The centre of the arts is the art center.",
];

const CHECK: Check = Check {
	// TODO: add more BE, UE, even generalize [a-z]+(ize|ized|izing)?
	check_type: CheckType::Consistency { word_pairs: &[
		("advisor", "adviser"),
		// ("analyse", "analyze"),
		("centre", "center"),
		("colour", "color"),
		("emphasise", "emphasize"),
		("finalise", "finalize"),
		("focussed", "focused"),
		("labour", "labor"),
		("learnt", "learned"),
		("organise", "organize"),
		("organised", "organized"),
		("organising", "organizing"),
		("recognise", "recognize"),
	] },
	path: "consistency.spelling",
	msg: "Inconsistent spelling of '{}' (vs. '{}').",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
