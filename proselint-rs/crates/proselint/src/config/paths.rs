use std::{env::current_dir, fs::create_dir_all, path::PathBuf};

use lazy_static::lazy_static;

#[cfg(feature = "demo")]
pub const DEMO_DATA: &str = include_str!("../../demo.md");

lazy_static! {
	static ref HOME_PATH: PathBuf = dirs::home_dir().unwrap();
	static ref CACHE_BASE_PATH: PathBuf = dirs::cache_dir().unwrap_or_else(|| {
		let target_path = HOME_PATH.join(".cache");
		create_dir_all(target_path.as_path()).unwrap();
		target_path
	});
	static ref CONFIG_BASE_PATH: Option<PathBuf> = dirs::config_dir();
	static ref CWD_PATH: Option<PathBuf> = current_dir().ok();

	pub static ref CACHE_PATH: PathBuf = {
		let cache_path = CACHE_BASE_PATH.join("proselint");
		create_dir_all(cache_path.as_path()).unwrap();
		cache_path
	};
	pub static ref CONFIG_GLOBAL_PATH: PathBuf = PathBuf::from("/etc/proselintrc");
	/// Config priority: cwd -> xdg config -> home
	pub static ref CONFIG_USER_PATHS: Vec<PathBuf> = {
		let config_names = [".proselintrc", ".proselint", "proselint"];
		let mut paths = Vec::with_capacity(8);
		if let Some(cwd_path) = CWD_PATH.clone() {
			paths.extend(config_names.map(|x| cwd_path.join(x)));
		}
		if let Some(config_path) = CONFIG_BASE_PATH.clone() {
			paths.extend([config_path.join("proselint/config"), config_path.join("proselint")]);
		}
		paths.extend(config_names.map(|x| HOME_PATH.join(x)));
		paths
	};
}
