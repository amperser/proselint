# Look for prose issues
prose.lint_files

warn "PR is classed as Work in Progress" if github.pr_title.include? "[WIP]"

if commits.any? { |c| c.message =~ /^Merge branch 'master'/ }
   warn 'Please rebase to get rid of the merge commits in this PR'
end
