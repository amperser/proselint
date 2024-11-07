use std::{collections::HashMap, path::PathBuf};

use clap::ValueEnum;
use config::{File, FileFormat};
use serde::{Deserialize, Serialize};

use super::paths::{CONFIG_GLOBAL_PATH, CONFIG_USER_PATHS};

const DEFAULT_CONFIG: &str = include_str!("./default.toml");

#[derive(Clone, Copy, Debug, Default, ValueEnum, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum OutputFormat {
	#[default]
	Full,
	// tODO: maybe this could serve as basis for lsp?
	Json,
	Compact,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Config {
	max_errors: u16,
	parallelize: bool,
	output_format: OutputFormat,
	checks: HashMap<String, bool>,
}

impl Config {
	pub fn max_errors(&self) -> u16 {
		self.max_errors
	}

	pub fn parallelize(&self) -> bool {
		self.parallelize
	}

	pub fn output_format(&self) -> OutputFormat {
		self.output_format
	}

	pub fn set_output_format(&mut self, output_format: OutputFormat) {
		self.output_format = output_format
	}

	pub fn checks(&self) -> &HashMap<String, bool> {
		&self.checks
	}

	pub fn checks_mut(&mut self) -> &mut HashMap<String, bool> {
		&mut self.checks
	}

	pub fn enabled_checks(&self) -> Vec<String> {
		self.checks
			.iter()
			.filter_map(|(name, enabled)| enabled.then_some(name.to_owned()))
			.collect()
	}
}

impl Default for Config {
	fn default() -> Self {
		toml::from_str(DEFAULT_CONFIG).unwrap()
	}
}

pub fn load_config(path: Option<PathBuf>) -> Config {
	let mut config_builder = config::Config::builder()
		.add_source(File::from_str(DEFAULT_CONFIG, FileFormat::Toml))
		.add_source(
			File::with_name(CONFIG_GLOBAL_PATH.to_str().unwrap())
				.required(false),
		);
	for user_path in CONFIG_USER_PATHS.iter() {
		config_builder = config_builder.add_source(
			File::with_name(user_path.to_str().unwrap()).required(false),
		);
	}
	if let Some(cli_path) = path {
		config_builder = config_builder
			.add_source(File::with_name(cli_path.to_str().unwrap()));
	}

	config_builder.build().and_then(config::Config::try_deserialize).unwrap()
}
