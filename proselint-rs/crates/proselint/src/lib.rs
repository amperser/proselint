use std::{path::PathBuf, process::ExitCode};

use args::{Args, Command};
use config::base::{load_config, Config, OutputFormat};

pub mod args;
pub mod config;
pub mod utils;

#[derive(Copy, Clone)]
pub enum ExitStatus {
	/// Linting was successful and there were no errors.
	Success = 0,
	/// Linting was successful but there were errors.
	Failure = 1,
	/// Linting failed.
	Error = 2,
}

impl From<ExitStatus> for ExitCode {
	fn from(value: ExitStatus) -> Self {
		ExitCode::from(value as u8)
	}
}

fn benchmark() {}

fn clean() {}

fn dump_config(
	config: Config,
	default: bool,
	#[cfg(feature = "json_config")] json: bool,
) {
	let config_version = if default { Config::default() } else { config };
	#[cfg(feature = "json_config")]
	if json {
		return println!(
			"{}",
			serde_json::to_string_pretty(&config_version).unwrap()
		);
	}
	println!("{}", toml::to_string_pretty(&config_version).unwrap())
}

fn check(
	config: Config,
	paths: Option<Vec<PathBuf>>,
	#[cfg(feature = "demo")] demo: bool,
) -> anyhow::Result<ExitStatus> {
	let results = crate::utils::lint_path(
		paths.unwrap_or(vec![]),
		config,
		#[cfg(feature = "demo")]
		demo,
	);
	print!("{results:?}");
	Ok(ExitStatus::Success)
}

// TODO: this
fn set_verbosity(_: bool) {}

pub fn run(Args { command, global_args }: Args) -> anyhow::Result<ExitStatus> {
	let default_panic_hook = std::panic::take_hook();
	std::panic::set_hook(Box::new(move |info| {
		eprintln!(r"error: proselint crashed");
		default_panic_hook(info);
	}));

	set_verbosity(global_args.verbose);

	let subcommand = command.unwrap_or_default();
	let mut config = load_config(global_args.config);
	if let Some(output_format) = global_args.output_format {
		config.set_output_format(output_format);
	} else if global_args.verbose {
		config.set_output_format(OutputFormat::Full)
	}

	match subcommand {
		Command::Benchmark => benchmark(),
		Command::Clean => clean(),
		Command::DumpConfig {
			default,
			#[cfg(feature = "json_config")]
			json,
		} => dump_config(
			config,
			default,
			#[cfg(feature = "json_config")]
			json,
		),
		Command::Check {
			paths,
			#[cfg(feature = "demo")]
			demo,
		} => {
			return check(
				config,
				paths,
				#[cfg(feature = "demo")]
				demo,
			)
		}
	}

	Ok(ExitStatus::Success)
}
