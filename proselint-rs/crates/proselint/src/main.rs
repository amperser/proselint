use std::process::ExitCode;

use clap::Parser;
use proselint::{args::Args, run, ExitStatus};

fn main() -> ExitCode {
	let args = Args::parse();
	match run(args) {
		Ok(code) => code.into(),
		Err(err) => {
			eprintln!("proselint failed");
			for cause in err.chain() {
				eprintln!("Cause: {cause}")
			}
			ExitStatus::Error.into()
		}
	}
}
