SublimeLinter-contrib-proselint
================================

[![Build Status](https://travis-ci.org/amperser/proselint.svg?branch=master)](https://travis-ci.org/amperser/proselint)

This linter plugin for [SublimeLinter][docs] provides an interface to [proselint](http://proselint.com). It will be used with files that have the “markdown”, “text”, or “plain text” syntaxes.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `proselint` is installed on your system. To install `proselint`, do the following:

1. Install [Python](http://python.org/download/) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `proselint` by typing the following in a terminal:
   ```
   [sudo] pip install proselint
   ```

**Note:** This plugin requires `proselint` 0.3.4 or later.

### Linter configuration
In order for `proselint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `proselint`, you can proceed to install the SublimeLinter-contrib-proselint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `proselint`. Among the entries you should see `SublimeLinter-contrib-proselint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-proselint provides its own settings through a config file, `.proselintrc`.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the main repository, http://github.com/amperser/proselint. This plugin can be found in `/plugins/sublime/`
1. Hack on a separate topic branch off the latest `master`.
1. Commit to the topic branch and push it.
1. Create a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability; don’t be afraid to use it.
- Please use descriptive variable names. No abbreviations unless they are well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
