[Reference](https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/)

# How to undo (almost) anything with Git

## Undoing the Last Commit

`git reset --soft HEAD~1
`git reset --hard HEAD~1

## Undo a "public" change

**Scenario:** You just ran `git push`, sending your changes to GitHub, now you realize there’s a problem with one of those commits. You’d like to undo that commit.

**Undo with:** `git revert <SHA>`

**What's happening:** `git revert` will create a new commit that’s the opposite (or inverse) of the given SHA. If the old commit is “matter”, the new commit is "anti-matter"—anything removed in the old commit will be added in the new commit and anything added in the old commit will be removed in the new commit.

This is Git's safest, most basic "undo" scenario, because it doesn’t _alter_ history—so you can now `git push` the new “inverse” commit to undo your mistaken commit.

## Fix the last commit message

**Scenario:** You just typo’d the last commit message, you did `git commit -m "Fxies bug #42"` but before `git push` you realized that really should say “Fixes bug #42”.

**Undo with:** `git commit --amend` or `git commit --amend -m "Fixes bug #42"`

**What’s happening:** `git commit --amend` will update and replace the most recent commit with a new commit that combines any staged changes with the contents of the previous commit. With nothing currently staged, this just rewrites the previous commit message.

## Undo "local" changes

**Scenario:** The cat walked across the keyboard and somehow saved the changes, then crashed the editor. You haven’t committed those changes, though. You want to undo everything in that file—just go back to the way it looked in the last commit.

**Undo with:** `git checkout -- <bad filename>`

**What’s happening:** `git checkout` alters files in the working directory to a state previously known to Git. You could provide a branch name or specific SHA you want to go back to or, by default, Git will assume you want to checkout `HEAD`, the last commit on the currently-checked-out branch.

Keep in mind: any changes you “undo” this way are _really_ gone. They were never committed, so Git can’t help us recover them later. Be sure you know what you’re throwing away here! (Maybe use `git diff` to confirm.)

## Reset "local" changes

**Scenario:** You’ve made some commits locally (not yet pushed), but everything is terrible, you want to undo the last three commits—like they never happened.

**Undo with:** `git reset <last good SHA>` or `git reset --hard <last good SHA>`

**What’s happening:** `git reset` rewinds your repository’s history all the way back to the specified SHA. It’s as if those commits never happened. By default, `git reset` preserves the working directory. The commits are gone, but the _contents_ are still on disk. This is the safest option, but often, you’ll want to “undo” the commits _and_ the changes in one move—that’s what `--hard` does.

## Redo after undo "local"

**Scenario:** You made some commits, did a `git reset --hard` to “undo” those changes (see above), and _then_ realized: you want those changes back!

**Undo with:** `git reflog` and `git reset` or `git checkout`

**What’s happening:** `git reflog` is an amazing resource for recovering project history. You can recover _almost_ anything—anything you’ve committed—via the reflog.

You’re probably familiar with the `git log` command, which shows a list of commits. `git reflog` is similar, but instead shows a list of times when `HEAD` changed.

Some caveats:

- `HEAD` changes _only_.`HEAD` changes when you switch branches, make commits with `git commit` and un-make commits with `git reset`, but `HEAD` does _not_ change when you `git checkout -- <bad filename>` (from an earlier scenario—as mentioned before, those changes were never committed, so the reflog can’t help us recover those.
- `git reflog` doesn’t last forever. Git will periodically clean up objects which are “unreachable.” Don’t expect to find months-old commits lying around in the reflog forever.
- Your `reflog` is yours and yours alone. You can’t use `git reflog` to restore another developer’s un-pushed commits.

So… how do you use the reflog to "redo" a previously “undone” commit or commits? It depends on what exactly you want to accomplish:

- If you want to restore the project’s history as it was at that moment in time use `git reset --hard <SHA>`
- If you want to recreate one or more files in your working directory as they were at that moment in time, without altering history use `git checkout <SHA> -- <filename>`
- If you want to replay _exactly one_ of those commits into your repository use `git cherry-pick <SHA>`