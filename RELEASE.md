# Releasing a new version

1. Use [bumpversion](https://pypi.org/project/bumpversion/) to increase the patch, minor, or major version in accordance with what has changed since the previous release.
2. Update CHANGELOG.md to explain the most recent changes.
3. Open a pull request against `master`.
4. Merge the pull request into `master`.
5. Tag the merge commit with the new version number.
6. Push the tag.

The tagged version will be uploaded to PyPI automatically.
