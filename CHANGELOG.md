# Change Log

## [0.15.0](https://github.com/amperser/proselint/compare/0.14.0..v0.15.0) - 2025-11-14

### ⛰️  Features

- *(registry)* Add strict padding for checks ([#1428](https://github.com/amperser/proselint/issues/1428)) - ([f1894bc](https://github.com/amperser/proselint/commit/f1894bccf5cb9344eca5daba64ad0b3ec8577784))
- Override keys and dot-prop ([#1440](https://github.com/amperser/proselint/issues/1440)) - ([ddebe9f](https://github.com/amperser/proselint/commit/ddebe9f182ebd6fb152f7699dc3ad38cac16ebe5))
- Add flag to prevent filtering quotes in lintfile ([#1404](https://github.com/amperser/proselint/issues/1404)) - ([109f58f](https://github.com/amperser/proselint/commit/109f58f8c52ab2b2bf838ad94718e7ba6ca6d664))
- Implement check registry ([#1396](https://github.com/amperser/proselint/issues/1396)) - ([3bc0d13](https://github.com/amperser/proselint/commit/3bc0d1347eae8b13429507617719303b58677489))

### 🐛 Bug Fixes

- *(checks)* Ignore least and most in uncomparables after at ([#1433](https://github.com/amperser/proselint/issues/1433)) - ([b94542c](https://github.com/amperser/proselint/commit/b94542c66f2a176b77bc01060ff5389612b2c986))
- *(checks)* Allow very well in weasel_words ([#1426](https://github.com/amperser/proselint/issues/1426)) - ([616e855](https://github.com/amperser/proselint/commit/616e855bb1d29c9b98d11bbbc1e16f41c6da4f52))
- *(checks)* Resolve meantime/meanwhile conflict in misc.preferred_forms ([#1425](https://github.com/amperser/proselint/issues/1425)) - ([18ecce6](https://github.com/amperser/proselint/commit/18ecce6409ffd63c6a809e7668edf9e539cec6a2))
- *(registry)* [**breaking**] Remove results_limit ([#1421](https://github.com/amperser/proselint/issues/1421)) - ([d77cd1b](https://github.com/amperser/proselint/commit/d77cd1b8c8d2bfa8511a87d2607c6ed983f316b6))
- Move chocolatey to spelling.consistency ([#1432](https://github.com/amperser/proselint/issues/1432)) - ([7a2d503](https://github.com/amperser/proselint/commit/7a2d503b784d426d84f90f84a59c17361327dcd6))
- Simplify but check and properly count lines ([#1423](https://github.com/amperser/proselint/issues/1423)) - ([68be196](https://github.com/amperser/proselint/commit/68be19657cb304c97234ca8b6d7f97b958f2f2ee))
- Rectify capitalisation in preferred forms ([#1413](https://github.com/amperser/proselint/issues/1413)) - ([81d2ea1](https://github.com/amperser/proselint/commit/81d2ea15f164159f7ee1b2c7261e8c20c91d338d))
- Check venery-waxed return types ([#1414](https://github.com/amperser/proselint/issues/1414)) - ([b481488](https://github.com/amperser/proselint/commit/b4814886f6e7e6c270b135d1ce358ef455d589ae))
- Update Sublime plugin for SublimeLinter4 ([#1107](https://github.com/amperser/proselint/issues/1107)) - ([8df0966](https://github.com/amperser/proselint/commit/8df0966636f84f3b0746ef4647ab02a85ff7ba26))

### 🚜 Refactor

- *(cli)* Switch click -> argparse and add logging ([#1400](https://github.com/amperser/proselint/issues/1400)) - ([01b507e](https://github.com/amperser/proselint/commit/01b507e3d6eb23f21a009913556468c974b14082))
- *(config)* Remove unused copy import ([#1402](https://github.com/amperser/proselint/issues/1402)) - ([cd19388](https://github.com/amperser/proselint/commit/cd1938898b0523d0312071bba3032ae544c7975c))
- *(tools)* Upgrade internals ([#1399](https://github.com/amperser/proselint/issues/1399)) - ([d9db2c5](https://github.com/amperser/proselint/commit/d9db2c55dd1916b7cdb528f9c042ef09f588892f))
- Stabilise wire logging ([#1444](https://github.com/amperser/proselint/issues/1444)) - ([02e85a8](https://github.com/amperser/proselint/commit/02e85a8fe89e33f2e786cee33985741be7ecef0c))
- [**breaking**] Upgrade to python 3.10 ([#1435](https://github.com/amperser/proselint/issues/1435)) - ([1b986fe](https://github.com/amperser/proselint/commit/1b986fefe78492a94dde1c713300043dc21b1c1a))
- [**breaking**] Remove unused corpus scoring ([#1403](https://github.com/amperser/proselint/issues/1403)) - ([85fde74](https://github.com/amperser/proselint/commit/85fde74ca2166702267099ca14c865e814901564))
- Implement iterators for check results ([#1398](https://github.com/amperser/proselint/issues/1398)) - ([fa73970](https://github.com/amperser/proselint/commit/fa73970af1b3a39aa9c973782cc754753634b566))
- Modernise config ([#1394](https://github.com/amperser/proselint/issues/1394)) - ([0e1feba](https://github.com/amperser/proselint/commit/0e1feba9a4b1b7bc702bdddc1ebbcfcfb6836307))
- Tidy checks ([#1383](https://github.com/amperser/proselint/issues/1383)) - ([053295c](https://github.com/amperser/proselint/commit/053295cd316dc7ab53393489e94f8a981eace4f4))

### 📚 Documentation

- Update treewide documentation ([#1445](https://github.com/amperser/proselint/issues/1445)) - ([7296f20](https://github.com/amperser/proselint/commit/7296f204e524b3f277091e512af326dc776bd2c0))

### ⚡ Performance

- *(checks)* [**breaking**] Use dual engine system ([#1436](https://github.com/amperser/proselint/issues/1436)) - ([e12a943](https://github.com/amperser/proselint/commit/e12a943b86525bbebaede47bc34f7f6a70025109))
- *(cli)* Import version lazily ([#1438](https://github.com/amperser/proselint/issues/1438)) - ([7bfb8f1](https://github.com/amperser/proselint/commit/7bfb8f15d341ecae9163215346a8a2a84ed435df))
- *(registry)* Early exit matches_partial ([#1441](https://github.com/amperser/proselint/issues/1441)) - ([9fa6339](https://github.com/amperser/proselint/commit/9fa6339225b7ba64382f92c5a8686a5eefc442bf))
- *(tools)* Use bisect for boundary checks ([#1407](https://github.com/amperser/proselint/issues/1407)) - ([c80ef08](https://github.com/amperser/proselint/commit/c80ef0833da5c1d2730d761847af70bbd934f029))

### ⚙️ Miscellaneous Tasks

- *(gh)* Remove pr frontmatter - ([da58e87](https://github.com/amperser/proselint/commit/da58e8752898789d46b4b33f3421dddd1d997518))
- *(publish)* Bypass protections ([#1447](https://github.com/amperser/proselint/issues/1447)) - ([200a817](https://github.com/amperser/proselint/commit/200a8174dcd75bc857fc65b75e4e28ad846a9723))
- *(publish)* Fix release configurations ([#1446](https://github.com/amperser/proselint/issues/1446)) - ([79885f8](https://github.com/amperser/proselint/commit/79885f8cae206042c133b749d0cc99d7438fe756))
- Use nix for workflows ([#1416](https://github.com/amperser/proselint/issues/1416)) - ([9c24e8c](https://github.com/amperser/proselint/commit/9c24e8ced7253e059ef0ccee89c9b100bd5c9530))
- Update issue templates ([#1420](https://github.com/amperser/proselint/issues/1420)) - ([35e7686](https://github.com/amperser/proselint/commit/35e7686967545dc8440311948557970aed81ba17))
- Update workflows ([#1419](https://github.com/amperser/proselint/issues/1419)) - ([7280204](https://github.com/amperser/proselint/commit/7280204898a46da9a38a035267b5f11518776a14))
- Ignore .envrc and .direnv ([#1415](https://github.com/amperser/proselint/issues/1415)) - ([6bf7ab5](https://github.com/amperser/proselint/commit/6bf7ab5f3216cac18e3a665618ab58fbbceb6cc5))
- Remove danger ([#1384](https://github.com/amperser/proselint/issues/1384)) - ([def7995](https://github.com/amperser/proselint/commit/def7995436c75333d3333b82446ab43ea616cbe4))
- Update ci and flake ([#1386](https://github.com/amperser/proselint/issues/1386)) - ([35e48a0](https://github.com/amperser/proselint/commit/35e48a08aa7eebf0139aa7a86a57cb3b1b47534b))
- Update tooling ([#1381](https://github.com/amperser/proselint/issues/1381)) - ([9132ee4](https://github.com/amperser/proselint/commit/9132ee44ebb9265ab66841875fee75fa3e06f4a8))
- Remove duplicate items from lists ([#1369](https://github.com/amperser/proselint/issues/1369)) - ([f01742d](https://github.com/amperser/proselint/commit/f01742d683be956cec6964bad6f302aeecebe89a))
- Pin runner image versions ([#1368](https://github.com/amperser/proselint/issues/1368)) - ([03a7360](https://github.com/amperser/proselint/commit/03a73606ef052730b27cd0158d294e6845d80d32))

### Build

- Fix distribution ([#1417](https://github.com/amperser/proselint/issues/1417)) - ([481a2a6](https://github.com/amperser/proselint/commit/481a2a622c25513c390fcaea7a042ee7ae6210f9))

## New Contributors ❤️

* @renovate[bot] made their first contribution in [#1443](https://github.com/amperser/proselint/pull/1443)
* @drainpixie made their first contribution in [#1440](https://github.com/amperser/proselint/pull/1440)
* @Yoshanuikabundi made their first contribution in [#1107](https://github.com/amperser/proselint/pull/1107)
* @ferdnyc made their first contribution in [#1370](https://github.com/amperser/proselint/pull/1370)

## [proselint@0.14.0](https://github.com/amperser/proselint/compare/0.13.0...0.14.0)

### Bug Fixes

- now loads the default configuration if none is provided ([#1246](https://github.com/amperser/proselint/pull/1246))
- added support for hyphens in `lexical_illusions` ([#1344](https://github.com/amperser/proselint/pull/1344))

### Features

- additional spelling checks `ally_ly`, `ance_ence`, `ely_ly` and `ve_of` ([#1266](https://github.com/amperser/proselint/pull/1266))

## [proselint@0.13.0](https://github.com/amperser/proselint/compare/0.12.0...0.13.0)

### Bug Fixes

- made memoize safe for both arguments and keyword arguments ([#1217](https://github.com/amperser/proselint/pull/1217))

### Features

- now exports decorators that wrap meta-checks ([#1188](https://github.com/amperser/proselint/pull/1188)]

## [proselint@0.12.0](https://github.com/amperser/proselint/compare/0.11.3...0.12.0)

### Bug fixes

- make am_pm checks case-sensitive ([#620](https://github.com/amperser/proselint/pull/620))

### Features

- added `--dump-config` and `--dump-default-config` CLI arguments ([#1212](https://github.com/amperser/proselint/pull/1212))
- now exports `proselint.config.default` ([#1212](https://github.com/amperser/proselint/pull/1212))

### Breaking Changes

- `proselint.tools.lint` now takes a config object instead of using `load_options` ([#1212](https://github.com/amperser/proselint/pull/1212))

## [proselint@0.11.3](https://github.com/amperser/proselint/compare/0.11.2...0.11.3)

Note: This is a hotfix release.

### Bug fixes

- fix package bundling to include proselintrc ([#1195](https://github.com/amperser/proselint/pull/1195))

## [proselint@0.11.2](https://github.com/amperser/proselint/compare/0.11.1...0.11.2)

Note: This is a hotfix release.

### Bug fixes

- correct false positives in `lexical_illusions.misc` ([#1192](https://github.com/amperser/proselint/pull/1192))

## [proselint@0.11.1](https://github.com/amperser/proselint/compare/0.11.0...0.11.1)

### Bug fixes

- fix package metadata and pypi upload (hotfix release)

## [proselint@0.11.0](https://github.com/amperser/proselint/compare/0.10.2...0.11.0)

### Bug fixes

- add warning for missing corpus ([535c330](https://github.com/amperser/proselint/commit/535c33095afacd6fbce4dcd428ffcffc01543077))
- reduce false positives for uncomparables.misc ([#1152](https://github.com/amperser/proselint/pull/1152))
- correct "attorney and not a republic" mondegreen ([#985](https://github.com/amperser/proselint/pull/985))
- correct unbound line and column in error printing ([#1181](https://github.com/amperser/proselint/pull/1181))
- fix false positive in `misc.but` ([#691](https://github.com/amperser/proselint/pull/691))

### Features

- add `--config` CLI argument ([#1081](https://github.com/amperser/proselint/pull/1081))
- add exceptions for `proselint.tools.existence_check` ([#1182](https://github.com/amperser/proselint/pull/1182))
- use regex for `lexical_illusions.misc` ([#1174](https://github.com/amperser/proselint/pull/1174))
- implement project-wide proselintrc ([#1173](https://github.com/amperser/proselint/pull/1173))

### Breaking Changes

N/A.

## [0.10.2](https://github.com/amperser/proselint/tree/0.10.2) (2018-08-03)
[Full Changelog](https://github.com/amperser/proselint/compare/0.10.1...0.10.2)

- Include tests in source package ([mavit](https://github.com/mavit))

## [0.10.1](https://github.com/amperser/proselint/tree/0.10.1) (2018-08-01)
[Full Changelog](https://github.com/amperser/proselint/compare/0.10.0...0.10.1)

- Support use as [pre-commit](https://pre-commit.com/) hook ([Andy Airey](https://github.com/aairey))

## [0.10.0](https://github.com/amperser/proselint/tree/0.10.0) (2018-07-23)
[Full Changelog](https://github.com/amperser/proselint/compare/0.9.0...0.10.0)

- Update dependencies to latest
- Add support for reading from stdin with the CLI ([io12](https://github.com/io12))
- Use pytest, not Nose, on Travis

## [0.9.0](https://github.com/amperser/proselint/tree/0.9.0) (2018-07-20)
[Full Changelog](https://github.com/amperser/proselint/compare/0.8.0...0.9.0)

- Add new plugins to README
- Update dependencies
- Comply with XDG spec ([xu-cheng](https://github.com/xu-cheng))

## [0.8.0](https://github.com/amperser/proselint/tree/0.8.0) (2017-02-22)
[Full Changelog](https://github.com/amperser/proselint/compare/0.7.0...0.8.0)

- Fix a cache-clearing issue ([m-charlton](https://github.com/m-charlton))
- Tons of improvements to tests ([joshmgrant](https://github.com/joshmgrant))
- New LGBTQ-terms module
- Misc. bug fixes and improvements
- Update various dependencies

## [0.7.0](https://github.com/amperser/proselint/tree/0.7.0) (2016-08-25)
[Full Changelog](https://github.com/amperser/proselint/compare/0.6.1...0.7.0)

**Implemented enhancements:**

- how about `typography.symbols` instead of `me.symbols` [\#373](https://github.com/amperser/proselint/issues/373)
- Improve test coverage [\#145](https://github.com/amperser/proselint/issues/145)
- Add a changelog [\#596](https://github.com/amperser/proselint/pull/596) ([suchow](https://github.com/suchow))

**Fixed bugs:**

- Exclamation point warning on all caps text [\#540](https://github.com/amperser/proselint/issues/540)
- proselint choked on bad character [\#504](https://github.com/amperser/proselint/issues/504)
- Could not open cache file [\#399](https://github.com/amperser/proselint/issues/399)

**Closed issues:**

- Add Instructions for Running Automated Tests on README [\#575](https://github.com/amperser/proselint/issues/575)
- Add the "real estate tycoon" to phrasal adjectives [\#543](https://github.com/amperser/proselint/issues/543)
- proselint CLI should append path to files [\#539](https://github.com/amperser/proselint/issues/539)
- Add "English-language learners" to phrasal adjectives [\#537](https://github.com/amperser/proselint/issues/537)
- Check out this Danger plugin [\#489](https://github.com/amperser/proselint/issues/489)
- No args leads to repeated messages: Exception TypeError: "'NoneType' object is not callable" in ignore [\#323](https://github.com/amperser/proselint/issues/323)
- Add rule on redundancies extracted from After the Deadline [\#279](https://github.com/amperser/proselint/issues/279)
- Add rule on "not guilty beyond a reasonable doubt" [\#242](https://github.com/amperser/proselint/issues/242)
- Eventually, submit to https://github.com/mcandre/linters [\#143](https://github.com/amperser/proselint/issues/143)
- Add check for Mondegreens [\#134](https://github.com/amperser/proselint/issues/134)

**Merged pull requests:**

- Ensure a clean commit history [\#592](https://github.com/amperser/proselint/pull/592) ([suchow](https://github.com/suchow))
- Remove Danger CI token [\#591](https://github.com/amperser/proselint/pull/591) ([suchow](https://github.com/suchow))
- Move Danger to Travis 'script' section [\#590](https://github.com/amperser/proselint/pull/590) ([suchow](https://github.com/suchow))
- more tests, all modules from C to L except links [\#589](https://github.com/amperser/proselint/pull/589) ([joshmgrant](https://github.com/joshmgrant))
- Add phrasal adj for issues \#543 and \#537 [\#588](https://github.com/amperser/proselint/pull/588) ([kylesezhi](https://github.com/kylesezhi))
- Added More Tests For Coverage [\#584](https://github.com/amperser/proselint/pull/584) ([joshmgrant](https://github.com/joshmgrant))
- added some instructions for running automated tests [\#581](https://github.com/amperser/proselint/pull/581) ([suchow](https://github.com/suchow))
- unintentionally unintentionally misspelled. [\#580](https://github.com/amperser/proselint/pull/580) ([suchow](https://github.com/suchow))
- unintentionally unintentionally misspelled. [\#579](https://github.com/amperser/proselint/pull/579) ([suchow](https://github.com/suchow))
- Update GitHub access token [\#578](https://github.com/amperser/proselint/pull/578) ([suchow](https://github.com/suchow))
- Add cats to list of venerys [\#568](https://github.com/amperser/proselint/pull/568) ([Decagon](https://github.com/Decagon))
- Add "kind of" and "mildly" to uncomparables [\#562](https://github.com/amperser/proselint/pull/562) ([Decagon](https://github.com/Decagon))
- Fix \#540 [\#557](https://github.com/amperser/proselint/pull/557) ([Decagon](https://github.com/Decagon))
- Survey improvements [\#554](https://github.com/amperser/proselint/pull/554) ([suchow](https://github.com/suchow))
- Use a more up-to-date link checker [\#553](https://github.com/amperser/proselint/pull/553) ([suchow](https://github.com/suchow))
- Fix a typo [\#552](https://github.com/amperser/proselint/pull/552) ([suchow](https://github.com/suchow))
- Add "color" to inconsistent spelling [\#547](https://github.com/amperser/proselint/pull/547) ([Decagon](https://github.com/Decagon))
- Danger [\#546](https://github.com/amperser/proselint/pull/546) ([suchow](https://github.com/suchow))
- Add Danger plugin to readme [\#545](https://github.com/amperser/proselint/pull/545) ([suchow](https://github.com/suchow))
- Removing relative directory line on extract\_files function in the command line interface [\#541](https://github.com/amperser/proselint/pull/541) ([CatherineH](https://github.com/CatherineH))
- Improve survey [\#538](https://github.com/amperser/proselint/pull/538) ([suchow](https://github.com/suchow))
- Bump version to 0.6.1 [\#531](https://github.com/amperser/proselint/pull/531) ([suchow](https://github.com/suchow))
- Guidelines based on GLAAD Media Reference [\#486](https://github.com/amperser/proselint/pull/486) ([joshmgrant](https://github.com/joshmgrant))

## [0.6.1](https://github.com/amperser/proselint/tree/0.6.1) (2016-07-18)
[Full Changelog](https://github.com/amperser/proselint/compare/0.6.0...0.6.1)

**Closed issues:**

- sort output by line number? [\#505](https://github.com/amperser/proselint/issues/505)

**Merged pull requests:**

- Pr/518 [\#529](https://github.com/amperser/proselint/pull/529) ([suchow](https://github.com/suchow))
- Test Case for `tools.consistency\_check` [\#522](https://github.com/amperser/proselint/pull/522) ([joshmgrant](https://github.com/joshmgrant))
- Testing for illegal utf-8 seq handling [\#520](https://github.com/amperser/proselint/pull/520) ([CraigKelly](https://github.com/CraigKelly))
- Remove skipping tests for preferred\_forms\_check [\#515](https://github.com/amperser/proselint/pull/515) ([joshmgrant](https://github.com/joshmgrant))
- Change file opening to replace characters on UTF-8 decode errors [\#514](https://github.com/amperser/proselint/pull/514) ([suchow](https://github.com/suchow))
- Sort output by line and column number [\#512](https://github.com/amperser/proselint/pull/512) ([vikasgorur](https://github.com/vikasgorur))
- typo? [\#507](https://github.com/amperser/proselint/pull/507) ([ivarvong](https://github.com/ivarvong))

## [0.6.0](https://github.com/amperser/proselint/tree/0.6.0) (2016-07-01)
[Full Changelog](https://github.com/amperser/proselint/compare/0.5.4...0.6.0)

**Closed issues:**

- Proselint doesn't work on readonly files [\#502](https://github.com/amperser/proselint/issues/502)
- Segmentation fault: 11 [\#487](https://github.com/amperser/proselint/issues/487)

**Merged pull requests:**

- Bump version to 0.6.0 [\#503](https://github.com/amperser/proselint/pull/503) ([suchow](https://github.com/suchow))

## [0.5.4](https://github.com/amperser/proselint/tree/0.5.4) (2016-06-28)
[Full Changelog](https://github.com/amperser/proselint/compare/0.5.3...0.5.4)

**Fixed bugs:**

- Remove `shell=True` as they are a security hazard [\#395](https://github.com/amperser/proselint/issues/395)

**Closed issues:**

- Speed up AppVeyor builds by caching [\#470](https://github.com/amperser/proselint/issues/470)
- Instructions for installing on OS X [\#457](https://github.com/amperser/proselint/issues/457)
- Wow [\#435](https://github.com/amperser/proselint/issues/435)
- OS X Installation issue [\#423](https://github.com/amperser/proselint/issues/423)
- Create a list of known automated grammar / usage checkers [\#281](https://github.com/amperser/proselint/issues/281)
- Checklist for open sourcing [\#198](https://github.com/amperser/proselint/issues/198)

**Merged pull requests:**

- Pr/376 [\#500](https://github.com/amperser/proselint/pull/500) ([suchow](https://github.com/suchow))
- Pr/481 [\#499](https://github.com/amperser/proselint/pull/499) ([suchow](https://github.com/suchow))
- Improve formatting of Josh Grant's cliches test [\#498](https://github.com/amperser/proselint/pull/498) ([suchow](https://github.com/suchow))
- Call load\_options\(\) once and save the results instead of calling it t… [\#493](https://github.com/amperser/proselint/pull/493) ([suchow](https://github.com/suchow))
- Fix typos [\#492](https://github.com/amperser/proselint/pull/492) ([jwilk](https://github.com/jwilk))
- Fixed spelling [\#482](https://github.com/amperser/proselint/pull/482) ([TalkingAvocado](https://github.com/TalkingAvocado))
- Tweak website [\#479](https://github.com/amperser/proselint/pull/479) ([suchow](https://github.com/suchow))
- Update Werkzeug version [\#478](https://github.com/amperser/proselint/pull/478) ([suchow](https://github.com/suchow))
- Tracebacks [\#475](https://github.com/amperser/proselint/pull/475) ([suchow](https://github.com/suchow))
- Add replacements to return value of checks [\#473](https://github.com/amperser/proselint/pull/473) ([suchow](https://github.com/suchow))
- Tests for existence\_check in tools.py [\#469](https://github.com/amperser/proselint/pull/469) ([joshmgrant](https://github.com/joshmgrant))
- Remove `shell=True` [\#467](https://github.com/amperser/proselint/pull/467) ([suchow](https://github.com/suchow))
- Fix typo in docstring [\#466](https://github.com/amperser/proselint/pull/466) ([suchow](https://github.com/suchow))
- Improve code coverage [\#465](https://github.com/amperser/proselint/pull/465) ([suchow](https://github.com/suchow))
- Update dependencies to latest versions [\#464](https://github.com/amperser/proselint/pull/464) ([suchow](https://github.com/suchow))
- Create a list of other usage & grammar tools [\#462](https://github.com/amperser/proselint/pull/462) ([suchow](https://github.com/suchow))
- Improve documentation [\#461](https://github.com/amperser/proselint/pull/461) ([suchow](https://github.com/suchow))
- Copyedit the readme [\#459](https://github.com/amperser/proselint/pull/459) ([suchow](https://github.com/suchow))
- Update Coveralls badge in readme [\#456](https://github.com/amperser/proselint/pull/456) ([suchow](https://github.com/suchow))
- Add link to Phabricator integration to readme [\#453](https://github.com/amperser/proselint/pull/453) ([suchow](https://github.com/suchow))
- Remove lintscore badge from README [\#452](https://github.com/amperser/proselint/pull/452) ([suchow](https://github.com/suchow))
- Allow proselintrc to be overriden by user [\#451](https://github.com/amperser/proselint/pull/451) ([suchow](https://github.com/suchow))
- Create test pattern for checks [\#450](https://github.com/amperser/proselint/pull/450) ([suchow](https://github.com/suchow))
- Add CodeClimate config file [\#449](https://github.com/amperser/proselint/pull/449) ([suchow](https://github.com/suchow))
- Do not open file for reading and writing [\#447](https://github.com/amperser/proselint/pull/447) ([Tatsh](https://github.com/Tatsh))
- Refactor tools [\#445](https://github.com/amperser/proselint/pull/445) ([suchow](https://github.com/suchow))

## [0.5.3](https://github.com/amperser/proselint/tree/0.5.3) (2016-04-05)
[Full Changelog](https://github.com/amperser/proselint/compare/0.5.2...0.5.3)

**Merged pull requests:**

- Bump version to 0.5.3 [\#448](https://github.com/amperser/proselint/pull/448) ([suchow](https://github.com/suchow))

## [0.5.2](https://github.com/amperser/proselint/tree/0.5.2) (2016-04-04)
[Full Changelog](https://github.com/amperser/proselint/compare/0.5.1...0.5.2)

**Implemented enhancements:**

- Make `proselint .` run over entire directory, possibly with a recursive option [\#292](https://github.com/amperser/proselint/issues/292)

**Merged pull requests:**

- Fix error message for phrasal-adj. hyphenation [\#444](https://github.com/amperser/proselint/pull/444) ([suchow](https://github.com/suchow))
- Show status of master in AppVeyor badge [\#442](https://github.com/amperser/proselint/pull/442) ([suchow](https://github.com/suchow))
- Fix AppVeyor badge in readme [\#441](https://github.com/amperser/proselint/pull/441) ([suchow](https://github.com/suchow))
- Use AppVeyor for Windows CI [\#440](https://github.com/amperser/proselint/pull/440) ([suchow](https://github.com/suchow))
- Handle missing dbm module on some python 2.7 systems [\#439](https://github.com/amperser/proselint/pull/439) ([CraigKelly](https://github.com/CraigKelly))

## [0.5.1](https://github.com/amperser/proselint/tree/0.5.1) (2016-04-02)
[Full Changelog](https://github.com/amperser/proselint/compare/0.5.0...0.5.1)

**Fixed bugs:**

- JSON flag gives incorrect line/column numbers [\#418](https://github.com/amperser/proselint/issues/418)
- Exception TypeError: "'NoneType' object is not callable" in  ignored [\#238](https://github.com/amperser/proselint/issues/238)

**Merged pull requests:**

- Bump version to 0.5.1 [\#436](https://github.com/amperser/proselint/pull/436) ([suchow](https://github.com/suchow))
- Attempt to fix cache-related bugs [\#432](https://github.com/amperser/proselint/pull/432) ([CraigKelly](https://github.com/CraigKelly))
- Add entry to phrasal-adj. hyphenation check [\#431](https://github.com/amperser/proselint/pull/431) ([suchow](https://github.com/suchow))
- Fix off-by-one error in JSON output [\#429](https://github.com/amperser/proselint/pull/429) ([suchow](https://github.com/suchow))
- Don't warn when there's only 1 "!" [\#426](https://github.com/amperser/proselint/pull/426) ([laraross](https://github.com/laraross))

## [0.5.0](https://github.com/amperser/proselint/tree/0.5.0) (2016-03-31)
[Full Changelog](https://github.com/amperser/proselint/compare/0.4.4...0.5.0)

**Implemented enhancements:**

- Return a non-zero exit status when there are warnings [\#427](https://github.com/amperser/proselint/issues/427)

**Merged pull requests:**

- Use exit codes [\#428](https://github.com/amperser/proselint/pull/428) ([suchow](https://github.com/suchow))

## [0.4.4](https://github.com/amperser/proselint/tree/0.4.4) (2016-03-30)
[Full Changelog](https://github.com/amperser/proselint/compare/0.4.3...0.4.4)

**Implemented enhancements:**

- Assorted issues from Debian mailing list [\#389](https://github.com/amperser/proselint/issues/389)

**Fixed bugs:**

- Typo on API page [\#417](https://github.com/amperser/proselint/issues/417)
- Assorted issues from Debian mailing list [\#389](https://github.com/amperser/proselint/issues/389)

**Merged pull requests:**

- Reorganization [\#424](https://github.com/amperser/proselint/pull/424) ([suchow](https://github.com/suchow))
- Update api.md - fixes \#417 [\#420](https://github.com/amperser/proselint/pull/420) ([shubheksha](https://github.com/shubheksha))
- added tests for butterick.symbols [\#413](https://github.com/amperser/proselint/pull/413) ([suchow](https://github.com/suchow))
- Deploy to PyPi only once [\#410](https://github.com/amperser/proselint/pull/410) ([suchow](https://github.com/suchow))
- Deploy to pypi automatically [\#409](https://github.com/amperser/proselint/pull/409) ([suchow](https://github.com/suchow))

## [0.4.3](https://github.com/amperser/proselint/tree/0.4.3) (2016-03-19)
[Full Changelog](https://github.com/amperser/proselint/compare/0.4.2...0.4.3)

## [0.4.2](https://github.com/amperser/proselint/tree/0.4.2) (2016-03-18)
[Full Changelog](https://github.com/amperser/proselint/compare/0.4.1...0.4.2)

**Merged pull requests:**

- Fixed exception in the TypeError handler when cache sync fails [\#408](https://github.com/amperser/proselint/pull/408) ([saul](https://github.com/saul))
- Set option name to json output [\#406](https://github.com/amperser/proselint/pull/406) ([marsam](https://github.com/marsam))

## [0.4.1](https://github.com/amperser/proselint/tree/0.4.1) (2016-03-18)
[Full Changelog](https://github.com/amperser/proselint/compare/0.4.0...0.4.1)

**Implemented enhancements:**

- explain corpora directory [\#357](https://github.com/amperser/proselint/issues/357)
- Add clean option to ensure that proselint clears cache before running [\#330](https://github.com/amperser/proselint/issues/330)
- Hide filename in log when linting individual files [\#317](https://github.com/amperser/proselint/issues/317)

**Fixed bugs:**

- Remove filthy language from demo and test site [\#347](https://github.com/amperser/proselint/issues/347)

**Closed issues:**

- 'bug' when run with op to terminal? [\#405](https://github.com/amperser/proselint/issues/405)
- Validity of Strunk & White as source [\#394](https://github.com/amperser/proselint/issues/394)
- Create plugin for Atom [\#371](https://github.com/amperser/proselint/issues/371)
- Add tex support for vim plugin [\#340](https://github.com/amperser/proselint/issues/340)
- Create plugin for emacs [\#37](https://github.com/amperser/proselint/issues/37)

**Merged pull requests:**

- Add check for 'But' at start of paragraph [\#404](https://github.com/amperser/proselint/pull/404) ([dhan12](https://github.com/dhan12))
- Fix the Vim plugin to work with older versions of syntastic [\#398](https://github.com/amperser/proselint/pull/398) ([lcd047](https://github.com/lcd047))
- Added check for inferior/superior to/than. [\#392](https://github.com/amperser/proselint/pull/392) ([tkmharris](https://github.com/tkmharris))
- Added a directory for checks from Fowler's. Added a check for 'waxed … [\#391](https://github.com/amperser/proselint/pull/391) ([tkmharris](https://github.com/tkmharris))
- Add check for nonwords [\#390](https://github.com/amperser/proselint/pull/390) ([suchow](https://github.com/suchow))
- Make it possible to run `proselint .` over a directory [\#388](https://github.com/amperser/proselint/pull/388) ([suchow](https://github.com/suchow))
- Add rule on 'geometer' [\#387](https://github.com/amperser/proselint/pull/387) ([suchow](https://github.com/suchow))
- Fix the Vim plugin [\#377](https://github.com/amperser/proselint/pull/377) ([lcd047](https://github.com/lcd047))
- Fix bug in version formatting [\#372](https://github.com/amperser/proselint/pull/372) ([suchow](https://github.com/suchow))
- Add a --compact flag [\#370](https://github.com/amperser/proselint/pull/370) ([suchow](https://github.com/suchow))
- Fix bug in garner.dates \#278 [\#369](https://github.com/amperser/proselint/pull/369) ([ksslng](https://github.com/ksslng))
- Fix bug in Travis yml [\#368](https://github.com/amperser/proselint/pull/368) ([suchow](https://github.com/suchow))
- Remove filth from demo [\#366](https://github.com/amperser/proselint/pull/366) ([suchow](https://github.com/suchow))
- Remove rogue print statement [\#365](https://github.com/amperser/proselint/pull/365) ([suchow](https://github.com/suchow))
- Create file in memory in worker function [\#363](https://github.com/amperser/proselint/pull/363) ([suchow](https://github.com/suchow))
- Fix bug in webapp [\#362](https://github.com/amperser/proselint/pull/362) ([suchow](https://github.com/suchow))
- Describe corpus in README [\#360](https://github.com/amperser/proselint/pull/360) ([laraross](https://github.com/laraross))
- Add check for 'not guilty beyond a reasonable doubt' [\#359](https://github.com/amperser/proselint/pull/359) ([suchow](https://github.com/suchow))
- Update commercialese.py [\#354](https://github.com/amperser/proselint/pull/354) ([ciarand](https://github.com/ciarand))
- Fix backwards reference [\#353](https://github.com/amperser/proselint/pull/353) ([drinks](https://github.com/drinks))
- Fix spelling of kaleidoscope [\#352](https://github.com/amperser/proselint/pull/352) ([drinks](https://github.com/drinks))
- Correct duplicate docstrings [\#351](https://github.com/amperser/proselint/pull/351) ([hugovk](https://github.com/hugovk))
- Fix misattributed Twain quote [\#350](https://github.com/amperser/proselint/pull/350) ([hugovk](https://github.com/hugovk))
- Fix typo of garner in three checks' error messages [\#349](https://github.com/amperser/proselint/pull/349) ([stig](https://github.com/stig))
- Github -\> GitHub typos [\#348](https://github.com/amperser/proselint/pull/348) ([hugovk](https://github.com/hugovk))

## [0.4.0](https://github.com/amperser/proselint/tree/0.4.0) (2016-03-08)
[Full Changelog](https://github.com/amperser/proselint/compare/0.3.5...0.4.0)

**Implemented enhancements:**

- Proselint's SublimeText plugin is not on Package Control [\#234](https://github.com/amperser/proselint/issues/234)

**Fixed bugs:**

- Short flags are broken [\#326](https://github.com/amperser/proselint/issues/326)
- trigger happy on exclamation mark warnings [\#322](https://github.com/amperser/proselint/issues/322)
- proselint --initialize throws errors [\#304](https://github.com/amperser/proselint/issues/304)
- Add -h argument option and double dash single character options [\#303](https://github.com/amperser/proselint/issues/303)
- Enforce compatibility with Python 2 and 3 [\#297](https://github.com/amperser/proselint/issues/297)
- Remove newline characters from error messages [\#288](https://github.com/amperser/proselint/issues/288)

**Closed issues:**

- Add LICENSE.md and README.md to source distribution [\#343](https://github.com/amperser/proselint/issues/343)
- Website Lintscore Error [\#319](https://github.com/amperser/proselint/issues/319)
- Vim Plugin [\#309](https://github.com/amperser/proselint/issues/309)
- broken link http://amzn.to/15wF76r [\#298](https://github.com/amperser/proselint/issues/298)
- Extract rules from the Federal Plain Language Guidelines [\#255](https://github.com/amperser/proselint/issues/255)
- Create plugin for Atom editor [\#36](https://github.com/amperser/proselint/issues/36)

**Merged pull requests:**

- v0.4.0 [\#346](https://github.com/amperser/proselint/pull/346) ([suchow](https://github.com/suchow))
- Add README.md and LICENSE.md to source distribution [\#344](https://github.com/amperser/proselint/pull/344) ([viccuad](https://github.com/viccuad))
- Only complain about punctuational exclamation marks. Fixes \#322 [\#339](https://github.com/amperser/proselint/pull/339) ([jsenn](https://github.com/jsenn))
- Update site table [\#338](https://github.com/amperser/proselint/pull/338) ([michaelpacer](https://github.com/michaelpacer))
- Add list of available plugins to README [\#337](https://github.com/amperser/proselint/pull/337) ([suchow](https://github.com/suchow))
- added clean mode to build with no cache [\#332](https://github.com/amperser/proselint/pull/332) ([michaelpacer](https://github.com/michaelpacer))
- add short option to show help [\#329](https://github.com/amperser/proselint/pull/329) ([jstewmon](https://github.com/jstewmon))
- use absolute import to find proselint.tools [\#328](https://github.com/amperser/proselint/pull/328) ([jstewmon](https://github.com/jstewmon))
- fix click option declarations [\#327](https://github.com/amperser/proselint/pull/327) ([jstewmon](https://github.com/jstewmon))
- Fix miscalculation in lintscore example [\#324](https://github.com/amperser/proselint/pull/324) ([suchow](https://github.com/suchow))
- Update site only on master [\#321](https://github.com/amperser/proselint/pull/321) ([suchow](https://github.com/suchow))
- support variadic file args and stdin [\#320](https://github.com/amperser/proselint/pull/320) ([jstewmon](https://github.com/jstewmon))
- Correct spelling of "multiplication" [\#318](https://github.com/amperser/proselint/pull/318) ([fdb](https://github.com/fdb))
- Spelling corrections on page 'checks' [\#311](https://github.com/amperser/proselint/pull/311) ([TKAB](https://github.com/TKAB))
- v0.3.6 [\#307](https://github.com/amperser/proselint/pull/307) ([suchow](https://github.com/suchow))
- Update Flask-Limiter to latest version [\#302](https://github.com/amperser/proselint/pull/302) ([suchow](https://github.com/suchow))
- Update dependencies to latest [\#301](https://github.com/amperser/proselint/pull/301) ([suchow](https://github.com/suchow))
- Clean up source URLs and attributions [\#299](https://github.com/amperser/proselint/pull/299) ([suchow](https://github.com/suchow))
- Curly-quote max [\#296](https://github.com/amperser/proselint/pull/296) ([suchow](https://github.com/suchow))
- Don't flag 'matrices' [\#294](https://github.com/amperser/proselint/pull/294) ([suchow](https://github.com/suchow))
- Add rule on the redundant 'collocated together' [\#291](https://github.com/amperser/proselint/pull/291) ([suchow](https://github.com/suchow))
- Don't print errors object in json output [\#290](https://github.com/amperser/proselint/pull/290) ([marsam](https://github.com/marsam))
- Kill newline characters and whitespace in errors [\#289](https://github.com/amperser/proselint/pull/289) ([suchow](https://github.com/suchow))
- Add Flycheck plugin [\#287](https://github.com/amperser/proselint/pull/287) ([suchow](https://github.com/suchow))
- Add clichés from GNU diction [\#284](https://github.com/amperser/proselint/pull/284) ([suchow](https://github.com/suchow))
- Add check for diacritical marks [\#280](https://github.com/amperser/proselint/pull/280) ([suchow](https://github.com/suchow))
- Use subdirectories for posts [\#274](https://github.com/amperser/proselint/pull/274) ([suchow](https://github.com/suchow))
- Require a number on either side [\#273](https://github.com/amperser/proselint/pull/273) ([suchow](https://github.com/suchow))
- Skunked terms [\#270](https://github.com/amperser/proselint/pull/270) ([suchow](https://github.com/suchow))
- Allow no space around x in multiplication [\#269](https://github.com/amperser/proselint/pull/269) ([suchow](https://github.com/suchow))
- Add rule on false plurals [\#268](https://github.com/amperser/proselint/pull/268) ([suchow](https://github.com/suchow))
- Add stub for phrasal adjectives [\#267](https://github.com/amperser/proselint/pull/267) ([suchow](https://github.com/suchow))
- Improve typography checks [\#266](https://github.com/amperser/proselint/pull/266) ([suchow](https://github.com/suchow))
- Add stub of rule for professions [\#265](https://github.com/amperser/proselint/pull/265) ([suchow](https://github.com/suchow))
- Remove bare except clauses [\#264](https://github.com/amperser/proselint/pull/264) ([Uran198](https://github.com/Uran198))
- Upgrade to latest version of requirements [\#262](https://github.com/amperser/proselint/pull/262) ([suchow](https://github.com/suchow))
- Add instructions for Vim plug-in [\#258](https://github.com/amperser/proselint/pull/258) ([Carreau](https://github.com/Carreau))
- enable testing on Python 3.5 [\#257](https://github.com/amperser/proselint/pull/257) ([Carreau](https://github.com/Carreau))
- add a vim syntastic checker [\#256](https://github.com/amperser/proselint/pull/256) ([Carreau](https://github.com/Carreau))
- Add rule on "nouveau riche" [\#251](https://github.com/amperser/proselint/pull/251) ([suchow](https://github.com/suchow))
- Use Jekyll v2.5.3 [\#250](https://github.com/amperser/proselint/pull/250) ([suchow](https://github.com/suchow))
- Use bumpversion to manage versions [\#241](https://github.com/amperser/proselint/pull/241) ([suchow](https://github.com/suchow))
- Bump version number to 0.3.5 [\#240](https://github.com/amperser/proselint/pull/240) ([suchow](https://github.com/suchow))

## [0.3.5](https://github.com/amperser/proselint/tree/0.3.5) (2015-10-20)
[Full Changelog](https://github.com/amperser/proselint/compare/0.3.4...0.3.5)

**Fixed bugs:**

- Permission issues with current location of cache directory [\#225](https://github.com/amperser/proselint/issues/225)

**Merged pull requests:**

- Further copyedit Sublime Text plugin README [\#239](https://github.com/amperser/proselint/pull/239) ([suchow](https://github.com/suchow))
- Fix up the SublimeText README [\#237](https://github.com/amperser/proselint/pull/237) ([suchow](https://github.com/suchow))
- Fix bug in mondegreen rule [\#236](https://github.com/amperser/proselint/pull/236) ([suchow](https://github.com/suchow))
- Copy edit README for SublimeText plugin [\#235](https://github.com/amperser/proselint/pull/235) ([suchow](https://github.com/suchow))
- Update comment in butterick.symbols [\#233](https://github.com/amperser/proselint/pull/233) ([FakeYou](https://github.com/FakeYou))
- Add rule on mondegreens [\#232](https://github.com/amperser/proselint/pull/232) ([suchow](https://github.com/suchow))
- Fix for cache saving [\#231](https://github.com/amperser/proselint/pull/231) ([PatchRanger](https://github.com/PatchRanger))
- Fix bug in README formatting [\#230](https://github.com/amperser/proselint/pull/230) ([suchow](https://github.com/suchow))
- Add rule on 'neck-and-neck' [\#229](https://github.com/amperser/proselint/pull/229) ([suchow](https://github.com/suchow))
- Copy edit readme [\#228](https://github.com/amperser/proselint/pull/228) ([suchow](https://github.com/suchow))
- Update exclamation.py [\#226](https://github.com/amperser/proselint/pull/226) ([MichalPokorny](https://github.com/MichalPokorny))
- Fix version label [\#222](https://github.com/amperser/proselint/pull/222) ([suchow](https://github.com/suchow))
- Add rule on Wallace's examples of redundancy [\#221](https://github.com/amperser/proselint/pull/221) ([suchow](https://github.com/suchow))
- Revert "Enable all the checks by default" [\#220](https://github.com/amperser/proselint/pull/220) ([suchow](https://github.com/suchow))
- Fix autoresponder [\#219](https://github.com/amperser/proselint/pull/219) ([suchow](https://github.com/suchow))
- Tweak website [\#218](https://github.com/amperser/proselint/pull/218) ([suchow](https://github.com/suchow))
- Reinstate web app [\#216](https://github.com/amperser/proselint/pull/216) ([suchow](https://github.com/suchow))
- Misc. website improvements [\#215](https://github.com/amperser/proselint/pull/215) ([suchow](https://github.com/suchow))
- Update dependencies [\#214](https://github.com/amperser/proselint/pull/214) ([suchow](https://github.com/suchow))
- Remove live demo link, for now [\#213](https://github.com/amperser/proselint/pull/213) ([suchow](https://github.com/suchow))
- Further improve the README [\#212](https://github.com/amperser/proselint/pull/212) ([suchow](https://github.com/suchow))
- Update README [\#211](https://github.com/amperser/proselint/pull/211) ([suchow](https://github.com/suchow))
- Remove Heroku build from Travis [\#210](https://github.com/amperser/proselint/pull/210) ([suchow](https://github.com/suchow))
- Add stub for a rule on venery terms [\#209](https://github.com/amperser/proselint/pull/209) ([suchow](https://github.com/suchow))

## [0.3.4](https://github.com/amperser/proselint/tree/0.3.4) (2015-10-01)
[Full Changelog](https://github.com/amperser/proselint/compare/0.3.3...0.3.4)

**Merged pull requests:**

- Deploy to PyPi manually for now [\#207](https://github.com/amperser/proselint/pull/207) ([suchow](https://github.com/suchow))
- Fix some versioning issues [\#206](https://github.com/amperser/proselint/pull/206) ([suchow](https://github.com/suchow))

## [0.3.3](https://github.com/amperser/proselint/tree/0.3.3) (2015-09-30)
[Full Changelog](https://github.com/amperser/proselint/compare/0.3.2...0.3.3)

**Merged pull requests:**

- fixes version number [\#205](https://github.com/amperser/proselint/pull/205) ([michaelpacer](https://github.com/michaelpacer))

## [0.3.2](https://github.com/amperser/proselint/tree/0.3.2) (2015-09-30)
[Full Changelog](https://github.com/amperser/proselint/compare/0.3.1...0.3.2)

**Merged pull requests:**

- Disable version test [\#204](https://github.com/amperser/proselint/pull/204) ([laraross](https://github.com/laraross))
- fixup for pypi so demo will work [\#203](https://github.com/amperser/proselint/pull/203) ([laraross](https://github.com/laraross))
- Continuous integration [\#200](https://github.com/amperser/proselint/pull/200) ([suchow](https://github.com/suchow))

## [0.3.1](https://github.com/amperser/proselint/tree/0.3.1) (2015-09-30)
[Full Changelog](https://github.com/amperser/proselint/compare/0.3.0...0.3.1)

## [0.3.0](https://github.com/amperser/proselint/tree/0.3.0) (2015-09-30)
[Full Changelog](https://github.com/amperser/proselint/compare/0.2.1...0.3.0)

**Merged pull requests:**

- Get ready for PyPi [\#199](https://github.com/amperser/proselint/pull/199) ([suchow](https://github.com/suchow))

## [0.2.1](https://github.com/amperser/proselint/tree/0.2.1) (2015-09-30)
[Full Changelog](https://github.com/amperser/proselint/compare/0.2.0...0.2.1)

**Implemented enhancements:**

- Create a timing test on the command line [\#191](https://github.com/amperser/proselint/issues/191)

**Merged pull requests:**

- Add timing test to CLI [\#197](https://github.com/amperser/proselint/pull/197) ([suchow](https://github.com/suchow))
- Test proselint version number [\#196](https://github.com/amperser/proselint/pull/196) ([suchow](https://github.com/suchow))
- Print full email headers [\#195](https://github.com/amperser/proselint/pull/195) ([suchow](https://github.com/suchow))
- Fix bug in email bot [\#194](https://github.com/amperser/proselint/pull/194) ([suchow](https://github.com/suchow))
- Improve links [\#193](https://github.com/amperser/proselint/pull/193) ([suchow](https://github.com/suchow))
- Improve website copy [\#192](https://github.com/amperser/proselint/pull/192) ([suchow](https://github.com/suchow))
- Contributing recommendations [\#189](https://github.com/amperser/proselint/pull/189) ([laraross](https://github.com/laraross))
- Tweak license formatting [\#188](https://github.com/amperser/proselint/pull/188) ([laraross](https://github.com/laraross))
- Remove corpus [\#186](https://github.com/amperser/proselint/pull/186) ([laraross](https://github.com/laraross))
- Add CI token to Travis [\#185](https://github.com/amperser/proselint/pull/185) ([suchow](https://github.com/suchow))
- Don't run timing test [\#184](https://github.com/amperser/proselint/pull/184) ([suchow](https://github.com/suchow))
- add bsd license [\#181](https://github.com/amperser/proselint/pull/181) ([michaelpacer](https://github.com/michaelpacer))
- Move to proselint.com [\#180](https://github.com/amperser/proselint/pull/180) ([suchow](https://github.com/suchow))
- Move scoring into its own file [\#179](https://github.com/amperser/proselint/pull/179) ([suchow](https://github.com/suchow))
- Fix one more malapropism typo [\#178](https://github.com/amperser/proselint/pull/178) ([suchow](https://github.com/suchow))
- Fix typos [\#177](https://github.com/amperser/proselint/pull/177) ([suchow](https://github.com/suchow))
- Specify version of future in reqs. [\#174](https://github.com/amperser/proselint/pull/174) ([suchow](https://github.com/suchow))
- Remove 'll' from NFL's naughty words [\#173](https://github.com/amperser/proselint/pull/173) ([suchow](https://github.com/suchow))
- Beef up the README [\#172](https://github.com/amperser/proselint/pull/172) ([suchow](https://github.com/suchow))
- Consolidate hardcoding of version number [\#169](https://github.com/amperser/proselint/pull/169) ([suchow](https://github.com/suchow))

## [0.2.0](https://github.com/amperser/proselint/tree/0.2.0) (2015-09-18)
[Full Changelog](https://github.com/amperser/proselint/compare/v0.1.0...0.2.0)

**Closed issues:**

- should we delete the python3 branch now that it's complete? [\#157](https://github.com/amperser/proselint/issues/157)
- Add Louis C.K.'s rule on "the N-word" [\#154](https://github.com/amperser/proselint/issues/154)
- Upgrade to most recent version of dependencies [\#144](https://github.com/amperser/proselint/issues/144)
- Figure out the right name for a "check" [\#21](https://github.com/amperser/proselint/issues/21)
- Extract rules from DFW's dictionary in The Telegraph [\#4](https://github.com/amperser/proselint/issues/4)

**Merged pull requests:**

- Daily GMAUs [\#160](https://github.com/amperser/proselint/pull/160) ([suchow](https://github.com/suchow))
- Add Louis C.K.'s rule on the n-word [\#159](https://github.com/amperser/proselint/pull/159) ([suchow](https://github.com/suchow))
- Python3 [\#156](https://github.com/amperser/proselint/pull/156) ([michaelpacer](https://github.com/michaelpacer))
- Update requirements [\#147](https://github.com/amperser/proselint/pull/147) ([suchow](https://github.com/suchow))
- Improve test coverage [\#146](https://github.com/amperser/proselint/pull/146) ([suchow](https://github.com/suchow))

## [v0.1.0](https://github.com/amperser/proselint/tree/v0.1.0) (2015-07-13)
**Implemented enhancements:**

- Move cache to a place where Heroku can see it [\#90](https://github.com/amperser/proselint/issues/90)
- Fork NLTK / TextBlob and speed up importing them [\#88](https://github.com/amperser/proselint/issues/88)

**Fixed bugs:**

- "every possible" flagged as comparing an uncomparable [\#129](https://github.com/amperser/proselint/issues/129)
- Make proselint work in normal install mode [\#91](https://github.com/amperser/proselint/issues/91)
- Decade detector false alarms on 50 cent posessive [\#82](https://github.com/amperser/proselint/issues/82)
- Fix web plugin's handling of Unicode [\#62](https://github.com/amperser/proselint/issues/62)

**Closed issues:**

- Extract business euphemisms from Inc article [\#136](https://github.com/amperser/proselint/issues/136)
- Refactor proselint/checks/norris/denizen\_labels.py from a D on Code Climate [\#127](https://github.com/amperser/proselint/issues/127)
- Refactor proselint/checks/garner/sexism.py from a D on Code Climate [\#126](https://github.com/amperser/proselint/issues/126)
- Refactor proselint/checks/butterick/symbols.py from a D on Code Climate [\#125](https://github.com/amperser/proselint/issues/125)
- Test ticket from Code Climate [\#124](https://github.com/amperser/proselint/issues/124)
- Create a linter email service [\#123](https://github.com/amperser/proselint/issues/123)
- Make a splash page to collect email addresses [\#102](https://github.com/amperser/proselint/issues/102)
- Get a logo [\#101](https://github.com/amperser/proselint/issues/101)
- Add rate limiting to API [\#100](https://github.com/amperser/proselint/issues/100)
- Use worker and web processes [\#96](https://github.com/amperser/proselint/issues/96)
- Issue with broken link parsing [\#84](https://github.com/amperser/proselint/issues/84)
- Extract rules from "Anguished English" [\#67](https://github.com/amperser/proselint/issues/67)
- Make pep8 and pep257 run cleanly [\#61](https://github.com/amperser/proselint/issues/61)
- Add rule about spelling names correctly [\#58](https://github.com/amperser/proselint/issues/58)
- Build online writing editor using http://codemirror.net/? [\#50](https://github.com/amperser/proselint/issues/50)
- Check out the cement framework for command line utilities [\#47](https://github.com/amperser/proselint/issues/47)
- False alarms, corpora, QA, and contributing back [\#45](https://github.com/amperser/proselint/issues/45)
- Create a .proselintrc file [\#39](https://github.com/amperser/proselint/issues/39)
- Create plugin for Sublime Text [\#35](https://github.com/amperser/proselint/issues/35)
- Create an API [\#33](https://github.com/amperser/proselint/issues/33)
- Using "a" vs. "an" [\#31](https://github.com/amperser/proselint/issues/31)
- Figure out test inheritance [\#30](https://github.com/amperser/proselint/issues/30)
- Great writing should come back nearly clean [\#25](https://github.com/amperser/proselint/issues/25)
- Don't lint quoted text [\#24](https://github.com/amperser/proselint/issues/24)
- Architecture for sharing processed data across rules [\#20](https://github.com/amperser/proselint/issues/20)
- It's et al., not et. al [\#18](https://github.com/amperser/proselint/issues/18)
- Sort errors by the position in which they occur [\#12](https://github.com/amperser/proselint/issues/12)
- Integrate into Sublime Text as a linter [\#11](https://github.com/amperser/proselint/issues/11)
- Extract rules from write-good [\#5](https://github.com/amperser/proselint/issues/5)
- working out how i can best contribute using github/git [\#3](https://github.com/amperser/proselint/issues/3)
- Create a plugin system [\#2](https://github.com/amperser/proselint/issues/2)
- Choose a sensible naming/numbering scheme for errors [\#1](https://github.com/amperser/proselint/issues/1)

**Merged pull requests:**

- Make compatible with Python 3 [\#95](https://github.com/amperser/proselint/pull/95) ([suchow](https://github.com/suchow))
- Change the sublime plugin file [\#53](https://github.com/amperser/proselint/pull/53) ([suchow](https://github.com/suchow))
- Create a plugin system [\#13](https://github.com/amperser/proselint/pull/13) ([suchow](https://github.com/suchow))
