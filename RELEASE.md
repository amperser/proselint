# Releasing a new version

1. Use bumpversion (`poetry run bumpversion`) to increase the patch, minor, or major version in accordance with what has changed since the previous release.
2. Update `CHANGELOG.md` to explain the changes since the last tag (only features and bug fixes) and amend the prior commit with `git commit --amend --no-edit`.
3. Delete the version tag and recreate it with `git tag --delete VERSION && git tag VERSION`.
4. Push to `main`, including tags.
5. Create a release on GitHub from the tag with the most recent version number as its name and the markdown from the new changelog entry as its description (you'll notice the format from other prior releases).

That's it, you're done! We will automate most of this process in the future, but that's it for now.
