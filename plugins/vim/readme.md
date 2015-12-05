# Proselint plug-in for Vim

Proselint plug-in for Vim is meant to work with
[Syntastic](http://vimawesome.com/plugin/syntastic), as well as `proselint`
executable already installed and on `$PATH`. Syntastic is a generic file-linter
framework which expose various configuration option, like on which kind of file
to run which linter, as well as on which even (save, load, ...) process the
current file. Refer to [Syntastic](http://vimawesome.com/plugin/syntastic) docs
for help with this.  

If you are a Vim user that you likely have a preferred way of managing your
plug-ins. Find the installation directory of **Syntastic** and copy/or link
this file in its `syntax_checkers/text` folder. 

Typically on unix-like system this will be
`~/.vim/bundle/syntastic/syntax_checkers/text/`. 

Restart your Vim session/reload your vim settings/plug-ins, and you should now
get Proselint hints in your text files. 

Feel free to submit enhancement to this plug-in. 

# Caveats

Depending on the Plug-ins Manager you use with Vim, Copying/linking this file
into the bundle directory might prevent the Syntactic plug-in to update. Most
Package manager should show an error on update if this is the case. 

Just remove the file, update and put it back in place if this ever happen. 
