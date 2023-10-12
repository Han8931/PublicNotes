---
tags:git
---
# Config and Init

## Git Config
- Config Levels:
	1. System: all users
	2. Global: all repositories of the current user
	3. Local: current repository 
-   Initial config setting
	1. `git config --global user.name "Han"` 
	2. `git config --global user.email han@google.com`
	3. `git config --global core.editor "nvim"` : set my default text editor
	4. `git config --global -e` : opens my global config  
	5. `git config --global core.autocrlf true/input` : `true` for Windows and `input` for Linux or MacOS
		- Carriage return (cr) : `\r` in Windows
		- Line feed (lf) : `\n`  new line
		- Linux systems use only lf, but Windows uses both.
- Change default branch name from master to main:
	- `git config --global init.defaultBranch main`
## Init 
- Initialize git for a new project:
	- `git init`: This creates a new subdirectory named `.git` that contains all of your necessary repository files — a Git repository skeleton.

# Add and Commit
- Staging area: allows us to review our modifications
	- `git add file1 file2`
	- Note that even if we remove some files (`rm somefile`), they will be still in the staging area. So we can undo the command by simply typing `git add removedfile`
	- `git ls-files` : list staged files
- If all modifications are good, then update it by using `git commit `
	- Even after we commit files, staging area is not flushed
	- Each commit contains an unique id and some information.
	- If we just commit then we can add short and long descriptions of the commit
	- `git commit -m "Short msg"`
	- We can skip the staging step (add) by using 
		- `git commit -am "Some msg"`
  
# File managements 
## Status Check
- `git status`
- `git status -s` : short output
	- First column: staging status 
	- Second column: working directory
- We can check modifications _before staging files_ by 
	- `git diff <id1> <id2>`
		- `git log --oneline`: to get commid id
		- `git diff d6f7974 f0d160f`
- How to check modified lines of _staged files_ instead of just checking modified staged file names?
	- `git diff --staged`
		```bash
		diff --git a/test1.py b/test1.py
		index c42bbf3..7c88a15 100644 # Metadata
		--- a/test1.py 
		+++ b/test1.py
		@@ -3,3 +3,4 @@ Second
		 Third
		 test
		 test
		+test
		```
- `a/test1.py`: old file
- `b/test1.py`: new file

## Ignore Files
- `.gitignore` example:

```
# ignore all .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf
```

## Remove Files
To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area) and then commit. The `git rm` command does that, and also _removes the file from your working directory so you don't see it as an untracked file the next time around._ If you simply remove the file from your working directory, it shows up under the “Changes not staged for commit” (that is, unstaged) area of your git status output:

- `git rm ` : remove files from both the working tree and the staging area
- The next time you commit, the file will be gone and no longer tracked. If you modified the file or had already added it to the staging area, you must force the removal with the `-f` option. This is a safety feature to prevent accidental removal of data that hasn't yet been recorded in a snapshot and that can't be recovered from Git.
- Another useful thing you may want to do is to _keep the file in your working tree but remove it from your staging area_. In other words, you may want to _keep the file on your hard drive but not have Git track it anymore_. This is particularly useful if you forgot to add something to your `.gitignore` file and accidentally staged it, like a large log file or a bunch of .a compiled files. To do this, use the `--cached` option: 
	- `git rm --cached <filename>` 
	- `git rm --cached -r bin/` : recursively remove only from the index 
	- `git rm -r --cached <folder>`
	- `git rm log/\*.log`
 
## Moving Files
Unlike many other VCSs, _Git doesn't explicitly track file movement_. If you rename a file in Git, no metadata is stored in Git that tells it you renamed the file. However, Git is pretty smart about figuring that out after the fact — we'll deal with detecting file movement a bit later. Thus it's a bit confusing that Git has a `mv` command. _If you want to rename a file in Git, you can run something like_:
- `git mv file_from file_to`
	- This is actually equivalent to:
		1. `mv README.md README`
		2. `git rm README.md`
		3. `git add README`
  

# View Command History

After you have created several commits, or if you have cloned a repository with an existing commit history, you’ll probably want to look back to see what has happened. The most basic and powerful tool to do this is the `git log` command.

By default, with no arguments, git log lists the commits made in that repository in reverse chronological order; that is, the most recent commits show up first. As you can see, this command lists each commit with its SHA-1 checksum, the author’s name and email, the date written, and the commit message.

A huge number and variety of options to the git log command are available to show you exactly what you’re looking for. Here, we’ll show you some of the most popular

One of the more helpful options is `-p` or `--patch`, _which shows the difference_ (the patch output) introduced in each commit. You can also limit the number of log entries displayed, such as using `-2` to show only the last two entries.
- `git log -p -2`
- `git log -3`: show only the most recent three commits
	- This is shortcut for `git log -n 3`
- `git log --oneline` : show only commit messages with id (unique identifier)
- `git log --oneline --reverse`
- `git show {id}` : 
	- id can be obtained by `git log --oneline`
	- or just type `git show HEAD~1` : `HEAD~1` means one position behind from the head commit
- If we wanna see the final output of the modification then type colon with fullname after head
	- `git show HEAD~1:test.py`
 
## Filter by Date

1.  The `--after` option allows you to view all commits made after the given date:

```git
git log --after="yyyy-mm-dd"
```

2.  We can include the `--before` option to filter commits within a range of dates:

```git
git log --after="yyyy-mm-dd" --before=="yyyy-mm-dd"
```

3.  For additional convenience try using verbal time references, such as "1 week ago" or "yesterday":

```git
git log --after="1 week ago" --before=="yesterday"
```
## Filter by Author
Use the `--author` flag to display commits only made by a specific author:

```git
git log --author="Smith"
```

This returns only the commits with an author name that includes `Smith`. This option also allows regular expressions if you’re interested in refining your author search even more.

## Search by Message
The `--grep` flag can be used to filter commits by message, allowing you to filter out a logical group of commits if your project used a specific convention for the commit messages. Usage is as follows:

```git
git log --grep="Bugfix"
```

This will display commits in the log with the text "Bugfix" in the commit message.

For case insensitive use it with `-i` flag. 


## Visualize Log View
- Git trees: `git ls-trees {id}`:
	- Commits 
	- Blobs: files
	- Trees: directories
	- Tags
 - `git log --graph`

# Undoing Things
At any stage, you may want to undo something. Here, we’ll review a few basic tools for undoing changes that you’ve made. Be careful, because you can’t always undo some of these undos. This is one of the few areas in Git where you may lose some work if you do it wrong.

One of the common undos takes place _when you commit too early and possibly forget to add some files, or you mess up your commit message_. If you want to redo that commit, make the additional changes you forgot, stage them, and commit again using the `--amend` option:
- `git commit --amend`
	- It will open a text editor. You can **revise the commit message** then.

This command takes your staging area and uses it for the commit. If you’ve made no changes since your last commit (for instance, you run this command immediately after your previous commit), then your snapshot will look exactly the same, and all you’ll change is your commit message. 

The same commit-message editor fires up, but it already contains the message of your previous commit. You can edit the message the same as always, but it overwrites your previous commit. 

As an example, if you commit and then realize you forgot to stage the changes in a file you wanted to add to this commit, you can do something like this:
```
git commit -m 'Initial commit'
git add forgotten_file
git commit --amend
```
You end up with a single commit — the second commit replaces the results of the first. Also note that if you don't want to edit your commit message, then amend with the `--no-edit` option:
- `git commit --amend --no-edit`

## Uncommit 
There are two methods: `reset` / `revert`
- `git reset <id> --hard`: Let's say I want to uncommit the latest two commits and go to the third commit. Then 
	- `git reset <id of the third commit> --hard`
	- `--hard`: 
- Be cautious, `reset` command is **extremely dangerous. Never reset the other's commits**. 
- While `git reset` does this by moving the current head of the branch back to the specified commit, thereby changing the commit history, `git revert` does this by creating a new commit that undoes the changes in the specified commit and so does not change the history.

## Unstaging a Staged File
The next two sections demonstrate how to work with your staging area and working directory changes. The nice part is that the command you use to determine the state of those two areas also reminds you how to undo changes to them. For example, let's say you’ve changed two files and want to commit them as two separate changes, but you accidentally type `git add *` and stage them both. How can you unstage one of the two? The git status command reminds you:
- `git reset HEAD <file>`

## Unmodifying a Modified File
What if you realize that _you don't want to keep your changes to the file_? How can you easily unmodify it — revert it back to what it looked like when you last committed (or initially cloned, or however you got it into your working directory)? Luckily, git status tells you how to do that, too. In the last example output, the unstaged area looks like this:
- `git checkout -- <file>`
	- It’s important to understand that `git checkout -- <file>` is a **dangerous command**. Any local changes you made to that file are gone — Git just replaced that file with the last staged or committed version.
	- A better approach is branching.

## Undoing things with _git restore_
The command `git restore` is an alternative to `git reset`. 

#### Unstaging a Staged File with git restore
- `git restore --staged file.py`

#### Unmodifying a Modified File with git restore
- `git restore <file>`
- Go to the previous commit: `git restore --source=HEAD~1 file1.py` 

# Stash 
Suppose you are implementing a new feature for your product. Your code is in progress and suddenly a customer escalation comes. Because of this, you have to _keep aside your new feature work for a few hours_. You cannot commit your partial code and also cannot throw away your changes. So _you need some temporary space_, where you can store your partial changes and later on commit it.

In Git, the stash operation takes your modified tracked files, stages changes, and saves them on a stack of unfinished changes that you can reapply at any time.

- `git stash`
	- The stashed files can be recovered even after applying the reset command
- `git stash apply`
	- To pop a specific stashed: `git stash apply stash@{0}`
- `git stash drop`: drop the latest stash. 

# Worktree
Let's say you were working on a new feature and got a message from your colleague asking for a hotfix for another branch (e.g., master branch). You may temp to use `git stash` or `checkout` to that branch. `git worktree` allows to manage multiple working trees.  By adding worktree, you can make your working dir untouched, but you can checkout to the target branch automatically.
- `git worktree list`
- `git worktree add <dir> <branch>`
- `git worktree remove <branch>`


# Remote Repository 

## Upload to GitHub:
- `git remote add origin [repository URL]`:
	- `origin` is kinda nickname of the URL
- `git push origin master`
- `git pull origin master`
## Change remote origin
- `git remote set-url origin [URL]`	
## Check git url
- `git config --get remote.origin.url`
- `git remote -v`
## Remove Remote
- `git remote remove <repo name>`

# Bare Repository 
## Remote Server Repository
We can create a remote repository in a server and connect to it as follows:
- Create a bare repository in the server:
	- `git init --bare <repo name>`
- Add the bare repository to the local repository:
	- `git remote add origin ssh://<user account>@<ip addr>/remote/dir/`
	- `git clone ssh://<user account>@<ip addr>/remote/dir/`

# Authentication
## Avoid authentication (password) in git push or git pull
git config credential.helper store
## In case I want to chagne...
`vim ~/.git-credentials`
## Timeout
`git config --global credential.helper 'cache --timeout=3000'`

# Tag
Git has the ability to tag specific points in a repository’s history as being important. Typically, people use this functionality to mark release points (`v1.0`, `v2.0` and so on).

Please refer [Semantic Versioning](https://semver.org/).

Git supports two types of tags: _lightweight_ and _annotated_. A lightweight tag is very much like a branch that doesn’t change — it’s just a pointer to a specific commit.
## Lightweight Tag
- `git tag <tag name> <branch name or commit ID>`
	- You can checkout to the tagged commit:
		- `git checkout <tag-name>`
- `git tag`: list tags
- Git has the ability to tag specific points in a repository’s history as being important. Typically, people use this functionality to mark release points (`v1.0`, `v2.0` and so on):
	- `git tag -l "v1.8.5*"`
 
## Annotated Tag

Annotated tags are stored as full objects in the Git database. They’re checksummed; contain the tagger name, email, and date; have a tagging message; and can be signed and verified with GNU Privacy Guard (GPG). It’s generally recommended that you create annotated tags so you can have all this information; but if you want a temporary tag or for some reason don’t want to keep the other information, lightweight tags are available too.

- `git tag -a 1.1.0 -m "Bug fix" <commit ID or branch>`:
	- `-a`: annotated 
	- `-m`: message
- `git tag -v 1.1.0`: show detailed information

## Push Tags to a Remote Repositories
- `git push --tags`

### Put More Information in GitHub
Just edit the tag information

# Pull Request





