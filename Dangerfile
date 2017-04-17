# Look for prose issues
prose.lint_files

# Ensure a clean commits history
if git.commits.any? { |c| c.message =~ /^Merge branch/ }
  fail('Please rebase to get rid of the merge commits in this PR')
end

warn "This PR does not yet have an assignee." unless github.pr_json["assignee"]
