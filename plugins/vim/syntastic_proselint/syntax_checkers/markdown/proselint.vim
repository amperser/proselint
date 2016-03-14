"============================================================================
"File:        proselint.vim
"Description: Syntax checking plugin for syntastic
"Author:      The Proselint team
"
"============================================================================

let s:ft = expand('<sfile>:p:h:t', 1)

if exists('g:loaded_syntastic_' . s:ft . '_proselint_checker') || !exists('g:_SYNTASTIC_VERSION')
    finish
endif
let g:loaded_syntastic_{s:ft}_proselint_checker = 1

if s:ft !=# 'text' && !syntastic#util#versionIsAtLeast(split(g:_SYNTASTIC_VERSION, '[.-]'), [3, 7, 0, 54])
    execute 'runtime! syntax_checkers/text/*.vim'
    execute 'runtime! syntax_checkers/' . s:ft . '/*.vim'
endif

if !exists('g:syntastic_' . s:ft . '_proselint_quiet_messages') && exists('g:syntastic_text_proselint_quiet_messages')
    let g:syntastic_{s:ft}_proselint_quiet_messages = deepcopy(g:syntastic_text_proselint_quiet_messages)
endif

call g:SyntasticRegistry.CreateAndRegisterChecker({
    \ 'filetype': s:ft,
    \ 'name': 'proselint',
    \ 'redirect': 'text/proselint'})

" vim: set sw=4 sts=4 et fdm=marker:
