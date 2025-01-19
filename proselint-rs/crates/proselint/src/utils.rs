use std::{collections::HashMap, path::PathBuf};

use proselint_registry::checks::{types::CheckType, Check, LintResult};
use rayon::prelude::*;
use walkdir::WalkDir;

use crate::config::base::Config;

const STRAIGHT_QUOTES: &'static str = "\"'";
const CURLY_QUOTES: &'static str = "“”";

const VALID_EXTENSIONS: &'static [&'static str] =
	&["md", "txt", "rtf", "html", "tex", "markdown"];

pub fn get_line_and_column(text: &str, pos: usize) -> (usize, usize) {
	if pos == 0 {
		return (0, 0);
	}
	let lines: Vec<&str> =
		text.split_at(pos as usize).0.split_inclusive("\n").collect();
	(lines.len() - 1, lines.last().unwrap().len())
}

pub fn check_quotes_match(chars: (char, char)) -> bool {
	(STRAIGHT_QUOTES.contains(chars.0) && chars.0 == chars.1)
		|| (CURLY_QUOTES.contains(chars.0)
			&& CURLY_QUOTES.contains(chars.1)
			&& chars.0 != chars.1)
}

// TODO: allow this to return unmatched spans, to provide a way to check for
// entries that are unmatched, like in misc.braces
pub fn find_spans(
	text: &str,
	pattern: &str,
	predicate: &dyn Fn((char, char)) -> bool,
) -> Vec<(usize, usize)> {
	let active: Vec<(char, usize)> = regex::Regex::new(pattern)
		.unwrap()
		.find_iter(text)
		.map(|m| (m.as_str().chars().next().unwrap(), m.start()))
		.collect();
	let mut prev: Vec<(char, usize)> = Vec::new();
	let mut spans: Vec<(usize, usize)> = Vec::new();
	for (character, span_end) in active {
		if let Some((_, span_start)) = prev
			.clone()
			.iter()
			.rev()
			.find(|(potential, _)| predicate((character, *potential)))
			.take()
		{
			prev.pop();
			spans.push((*span_start, span_end));
		} else {
			prev.push((character, span_end));
		}
	}
	spans
}

pub fn find_quoted_ranges(text: &str) -> Vec<(usize, usize)> {
	find_spans(text, "[\"'“”]", &check_quotes_match)
}

pub fn is_quoted(pos: usize, text: &str) -> bool {
	find_quoted_ranges(text)
		.iter()
		.any(|(start, end)| (start..end).contains(&&pos))
}

pub fn run_check(check: Check, text: &str, source: &str) -> Vec<LintResult> {
	check
		.check(text)
		.iter()
		.filter_map(|result| {
			let (line, column) = get_line_and_column(text, result.start_pos);
			if !is_quoted(result.start_pos, text) {
				Some(LintResult {
					check_name: result.check_name,
					message: result.message.clone(),
					source: source.to_string(),
					line,
					column: column + 1,
					start: result.start_pos,
					end: result.end_pos,
					extent: result.end_pos - result.start_pos,
					severity: "warning".to_string(),
					replacements: result.replacements.clone(),
				})
			} else {
				None
			}
		})
		.collect()
}

pub fn lint(
	text: &str,
	_config: Config,
	_source_name: &str,
	_allow_futures: bool,
) -> Vec<LintResult> {
	let text = &format!("\n{text}\n");

	// TODO: registry
	let checks: Vec<Check> = proselint_checks::REGISTER.to_vec();

	// TODO: parallelize
	let mut errors: Vec<LintResult> = checks
		.iter()
		.map(|check| run_check(*check, text, ""))
		.flatten()
		.collect();
	errors.sort_unstable_by_key(|x| (x.line, x.column));
	errors
}

pub fn extract_files(paths: Vec<PathBuf>) -> Vec<PathBuf> {
	let mut expanded_files: Vec<PathBuf> = vec![];
	for path in paths {
		if path.is_dir() {
			for entry in WalkDir::new(path).into_iter().filter_map(|e| e.ok()) {
				if entry.path().extension().is_some_and(|ext| {
					VALID_EXTENSIONS.contains(&ext.to_str().unwrap())
				}) {
					expanded_files.push(entry.into_path());
				}
			}
		} else {
			expanded_files.push(path);
		}
	}
	expanded_files
}

pub fn lint_path(
	paths: Vec<PathBuf>,
	config: Config,
	#[cfg(feature = "demo")] demo: bool,
) -> HashMap<PathBuf, Vec<LintResult>> {
	let paths = extract_files(paths);

	let mut results = HashMap::new();
	let mut _chars = 0;

	#[cfg(feature = "demo")]
	if demo {
		results.insert(
			PathBuf::from("<demo>"),
			lint(crate::config::paths::DEMO_DATA, config, "<demo>", false),
		);
		return results;
	}

	if paths.len() == 0 {
		let content = std::io::read_to_string(std::io::stdin()).unwrap();
		results.insert(
			PathBuf::from("<stdin>"),
			lint(&content, config, "<stdin>", false),
		);
	} else {
		for file in paths {
			let content = std::fs::read_to_string(file.clone()).unwrap();
			results.insert(
				file.clone(),
				lint(
					&content,
					config.clone(),
					file.canonicalize().unwrap().to_str().unwrap(),
					true,
				),
			);
			_chars += content.len();
		}
	}

	results
}
