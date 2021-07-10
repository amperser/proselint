# Releasing a new version

1. Update `CHANGELOG.md` to explain the changes since the last tag (only features, bug fixes, and breaking changes).
1. Use `./utils version <version>` (where version is `patch`, `minor`, or `major`) in accordance with what has changed since the previous release.
4. Push to `main`, including tags.
5. Create a release on GitHub from the new tag with the new version number as its name and the markdown from the new changelog entry as its description (you'll notice the format from other prior releases).

That's it, you're done!
