macro_rules! concat_slices {
	($ty:ty, $default:expr => $($slice:path),* $(,)*) => {{
		const __CONCAT_LEN: usize = 0 $(+ $slice.len() )*;
		const __CONCAT_RESULT: [$ty; __CONCAT_LEN] = {
			let mut result = [$default; __CONCAT_LEN];
			let mut result_idx = 0;
			$(
				let slice = $slice;
				let mut slice_idx = 0;
				while slice_idx < slice.len() {
					result[result_idx] = slice[slice_idx];
					slice_idx += 1;
					result_idx += 1;
				}
			)*
			result
		};
		__CONCAT_RESULT
	}};
}

macro_rules! gen_register {
	($($module:ident),* $(,)*) => {
		$(
			pub mod $module;
		)*
		pub const REGISTER: &[proselint_registry::checks::Check] = &concat_slices!(proselint_registry::checks::Check, proselint_registry::checks::Check::default() => $($module::REGISTER, )*);
	};
}

gen_register!(
	annotations,
	archaism,
	cliches,
	consistency,
	dates_times,
	hedging,
	industrial_language,
    lexical_illusions,
    malapropisms,
    misc,
);

pub mod mixed_metaphors;
pub mod mondegreens;
pub mod needless_variants;
pub mod nonwords;
pub mod oxymorons;
pub mod punctuation;
pub mod redundancy;
pub mod restricted;
pub mod scientific;
pub mod skunked_terms;
pub mod social_awareness;
pub mod spelling;
pub mod terms;
pub mod typography;
pub mod uncomparables;
pub mod weasel_words;
