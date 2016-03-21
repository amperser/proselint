# Proselint plugin for Vim

Proselint plugin for Vim is meant to work with [syntastic][syntastic], as well
as the `proselint` executable already installed and in your `$PATH`. Syntastic
is a generic file-linter framework which exposes various configuration
options, such as on which kind of file to run which linter, as well as
on which event (save, load, ...) to process the current file. Refer to
syntastic's docs for help with this.

If you are a Vim user then you likely have a preferred way of managing
your plugins. Copy or link `syntastic_proselint` next to your other Vim
plugins, and enable it in your plugin manager. This should add `proselint`
as a syntastic checker for filetypes `asciidoc`, `help`, `html`, `markdown`,
`nroff`, `pod`, `rst`, `tex`, `texinfo`, `text`, and `xhtml`. If you open a
file of the relevant type and run `:SyntasticInfo`, you should see `proselint`
listed among the available checkers.

Next, edit your `vimrc` and add `proselint` to
`g:syntastic_<filetype>_checkers` for the filetypes you plan to use, and
restart Vim. You should now be able to get Proselint hints about your text
files.

If you want syntastic to filter out the messages produced by
certain Proselint rules, add the IDs of the relevant rules to
`g:syntastic_text_proselint_quiet_messages` like this:
```vim
let g:syntastic_text_proselint_quiet_messages = {
    \ 'regex': [
    \   '\m^typography\.',
    \   '\m^twain\.damn\>',
    \ ] }
```
See `:h 'syntastic_quiet_messages'` in Vim for more information. See also
`:h pattern` if you need help with Vim's regular expressions.

By default `g:syntastic_text_proselint_quiet_messages` is used for all
filetypes known to the `proselint` checker, not just `text`.

Feel free to submit enhancement to this plugin.

[syntastic]: https://github.com/scrooloose/syntastic
