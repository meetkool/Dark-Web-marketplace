#!/bin/bash
# fix_author.sh - run from top of repo (use Git Bash / WSL)

OLD_EMAIL="gmfalme@duara.io"
CORRECT_NAME="meetkool"
CORRECT_EMAIL="lcs2021023@iiitl.ac.in"

# clean up any previous filter-branch backups
rm -rf .git/refs/original
git for-each-ref --format="%(refname)" refs/original | xargs -r -n1 git update-ref -d

# run filter-branch
git filter-branch -f --env-filter '
if [ "$GIT_COMMITTER_EMAIL" = "'"$OLD_EMAIL"'" ]; then
    export GIT_COMMITTER_NAME="'"$CORRECT_NAME"'"
    export GIT_COMMITTER_EMAIL="'"$CORRECT_EMAIL"'"
fi
if [ "$GIT_AUTHOR_EMAIL" = "'"$OLD_EMAIL"'" ]; then
    export GIT_AUTHOR_NAME="'"$CORRECT_NAME"'"
    export GIT_AUTHOR_EMAIL="'"$CORRECT_EMAIL"'"
fi
' --tag-name-filter cat -- --all

# verify (shows any remaining commits with old email)
echo "---- commits with OLD_EMAIL (should be none) ----"
git log --all --pretty=format:"%h %an <%ae> %ad %s" | grep -i "gmfalme@duara.io" || echo "None found."

# aggressive cleanup (optional)
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo "Done. If output looks good, force-push to remote (see instructions)."

