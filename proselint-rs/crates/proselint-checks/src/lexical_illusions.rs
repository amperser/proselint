use proselint_registry::checks::{Check, CheckType};

pub const EXAMPLES_PASS: &[&str] = &[
	"Smoke phrase with nothing flagged.",
	"And he's gone, gone with the breeze",
	"You should know that that sentence wasn't wrong.",
	"She had had dessert on the balcony.",
	"The practitioner's side",
	"An antimatter particle",
	"The theory",
	"She had coffee at the Foo-bar bar.",
	"Don't just play the game - play the game.",
	"Green greenery",
];
pub const EXAMPLES_FAIL: &[&str] = &[
    "Paris in the the springtime.",
    "You should know that that that was wrong.",
    "She had coffee at the Foo bar bar.",
    "She she coffee at the Foo-bar.",
    "After I write i write i write.",
    "That is an echo is an echo",
    "Don't miss the biggest illusion miss the biggest illusion.",
];

const CHECK: Check = Check {
	check_type: CheckType::ExistenceSimple {
        // NOTE: this can't be padded without mod -> \1
		pattern: r"\b(?<!\\|\-)(\w+(?:\s+\w+){0,3})(?:\s+\1)+\b",
		unicode: true,
		exceptions: &[r"^had had$", r"^that that$"],
	},
	path: "lexical_illusions.misc",
	msg: "There's a lexical illusion in '{}' - one or more words are repeated.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
