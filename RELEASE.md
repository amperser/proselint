# Releasing a new version

1. Create a new branch off master with the new version number.
2. Update CHANGELOG.md to explain the most recent changes.
3. Use [bumpversion](https://pypi.org/project/bumpversion/) to increase the patch, minor, or major version in accordance with what has changed since the previous release.
4. Open a pull request against `master`.
5. Merge the pull request into `master`.
6. Tag the merge commit with the new version number.
7. Push the tag. The tagged version will be uploaded to PyPI automatically.
8. Run Chandler (`chandler push`) to sync the changelog with GitHub releases.
