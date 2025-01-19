use std::path::PathBuf;

use clap::{Parser, Subcommand};

use crate::config::base::OutputFormat;

#[derive(Debug, Parser)]
#[command(version, about)]
pub struct Args {
	#[command(subcommand)]
	pub(crate) command: Option<Command>,
	#[clap(flatten)]
	pub(crate) global_args: GlobalArgs,
}

#[derive(Clone, Debug, Default, clap::Args)]
pub struct GlobalArgs {
	#[arg(long, value_name = "FILE", global = true)]
	pub config: Option<PathBuf>,
	#[arg(short, long, value_enum, global = true)]
	pub output_format: Option<OutputFormat>,
	#[arg(short, long, action = clap::ArgAction::SetTrue, global = true)]
	pub verbose: bool,
}

#[derive(Debug, Subcommand)]
pub enum Command {
	Benchmark,
	Check {
		#[cfg(feature = "demo")]
		#[arg(long)]
		demo: bool,
		paths: Option<Vec<PathBuf>>,
	},
	Clean,
	DumpConfig {
		/// Dump the default configuration
		#[arg(long, action = clap::ArgAction::SetTrue)]
		default: bool,
		/// Dump the configuration in JSON format
		#[cfg(feature = "json_config")]
		#[arg(long, action = clap::ArgAction::SetTrue)]
		json: bool,
	},
}

impl Default for Command {
	fn default() -> Self {
		Command::Check {
			#[cfg(feature = "demo")]
			demo: false,
			paths: None,
		}
	}
}
