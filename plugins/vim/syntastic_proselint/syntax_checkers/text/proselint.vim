"============================================================================
"File:        proselint.vim
"Description: Syntax checking plugin for syntastic
"Author:      The Proselint team
"
"============================================================================

if exists('g:loaded_syntastic_text_proselint_checker')
    finish
endif
let g:loaded_syntastic_text_proselint_checker = 1

if !exists('g:syntastic_text_proselint_sort')
    let g:syntastic_text_proselint_sort = 1
endif

let s:save_cpo = &cpo
set cpo&vim

function! SyntaxCheckers_text_proselint_GetLocList() dict
    let makeprg = self.makeprgBuild({})

    let errorformat = '%f:%l:%c: %m'

    return SyntasticMake({
        \ 'makeprg': makeprg,
        \ 'errorformat': errorformat,
        \ 'defaults': { 'type': 'W', 'subtype': 'Style' },
        \ 'preprocess': 'iconv',
        \ 'returns': [0, 1] })
endfunction

call g:SyntasticRegistry.CreateAndRegisterChecker({
    \ 'filetype': 'text',
    \ 'name': 'proselint'})

let &cpo = s:save_cpo
unlet s:save_cpo

" vim: set sw=4 sts=4 et fdm=marker:
