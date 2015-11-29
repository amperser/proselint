"============================================================================
"File:        proselint.vim
"Description: Syntax checking plugin for syntastic.vim
"Author:      The Proselint team
"
"============================================================================

if exists('g:loaded_syntastic_text_proselint_checker')
    finish
endif
let g:loaded_syntastic_text_proselint_checker = 1

let s:save_cpo = &cpo
set cpo&vim

function! SyntaxCheckers_text_proselint_GetLocList() dict
    let makeprg = self.makeprgBuild({'exe': 'proselint'})

    let errorformat = '%f:%l:%c:%m'

    return SyntasticMake({
        \ 'makeprg': makeprg,
        \ 'errorformat': errorformat,
        \ 'defaults': { 'type': 'Style' },
        \ 'returns': [0, 1]})
endfunction

call g:SyntasticRegistry.CreateAndRegisterChecker({
    \ 'filetype': 'text',
    \ 'name': 'proselint'})

let &cpo = s:save_cpo
unlet s:save_cpo
