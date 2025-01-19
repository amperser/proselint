use proselint_registry::checks::{Check, types::*, CheckFlags};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["I was at xyz and then all hell broke loose."];

const CHECK: Check = Check {
	check_type: &ExistenceSimple {
		pattern: "all hell broke loose",
		exceptions: &[],
	},
	path: "cliches.hell",
	msg: "Never use the words 'all hell broke loose'.",
	flags: CheckFlags { limit_results: 3, ppm_threshold: 0 },
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
