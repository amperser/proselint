use proselint_registry::checks::{Check, types::*, Padding};
use phf::phf_map;

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["It is an improprietous use."];

const CHECK: Check = Check {
	check_type: &PreferredFormsSimple {
		items: &phf_map!("improprietous" => "improper"),
		padding: Padding::WordsInText,
	},
	path: "misc.back_formations",
	msg: "Back-formation. '{}' is the preferred form.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
