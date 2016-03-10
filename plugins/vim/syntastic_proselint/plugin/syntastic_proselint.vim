"============================================================================
"File:        syntastic_proselint.vim
"Description: Syntax checking plugin for syntastic
"Author:      The Proselint team
"
"============================================================================

if exists('g:loaded_syntastic_proselint_plugin') || &compatible
    finish
endif
let g:loaded_syntastic_proselint_plugin = 1

if exists('g:syntastic_extra_filetypes')
    call add(g:syntastic_extra_filetypes, 'help')
else
    let g:syntastic_extra_filetypes = ['help']
endif

" vim: set sw=4 sts=4 et fdm=marker:
