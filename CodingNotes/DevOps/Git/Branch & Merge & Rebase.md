---
tags:git
---
# Branch

Branching means you diverge from the main line of development and continue to do work without messing with that main line.

```sh
git add README test.rb LICENSE
git commit -m 'Initial commit'
```

When you create the commit by running `git commit`, Git checksums each subdirectory (in this case, just the root project directory) and stores them as a tree object in the Git repository. Git then creates a commit object that has the metadata and a pointer to the root project tree so it can re-create that snapshot when needed.

Your Git repository now contains five objects: three blobs (each representing the contents of one of the three files), one tree that lists the contents of the directory and specifies which file names are stored as which blobs, and one commit with the pointer to that root tree and all the commit metadata.


- Master (main) branch: he default branch name in Git is master. As you start making commits, you’re given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically.
	- if i am working on a single branch, then this is the only branch
- Head: How does Git know what branch you’re currently on? It keeps a special _pointer_ called HEAD.
- Feature branch: this is an additional branch. By default, each branch has no access to other branches. 
- Base: The base is the branch that changes are based.

## Create a new branch :
- `git branch <branch name>`: Note that this command only creates a new branch, it didn't switch to that branch. 
	- If you wanna create a new branch and want to switch to that new branch at the same time:
	- `git checkout -b <newbranch>`
- `git branch <branch name> <commit id>` : based on a specific revision
- `git branch -v` : Show the last commit on each branch
- `git branch --merged`
- `git branch --no-merged`

## Switching branches:
- `git checkout <branch>` or `git switch <branch>`
	- This moves `HEAD` to point to that branch. 
	- `switch` is only for switching branches
	- Return to your previously checked out branch:
		- `git switch -`
- Renaming branches: `git branch -m <new-name>`
	- Renaming a remote branch is equal to delete and push again:
			1. `git push origin --delete <old-name> `
			2. `git push -u origin <new-name>`
		- `-u` : set as an upstream, this is where i want to push by default. It is identical to `--set-upstream`
- Track branch 
	- `git branch --track <local branch> <remote branch>`
	- By default, branches in Git have nothing to do with each other. However, when you tell a local branch to "track" a remote branch, you create a connection between these two branches. Your local branch now has a "counterpart" on the remote server.
	- `git checkout --track <remote branch>`
- Pulling+Pushing Branches:
	- `git pull`
	- `git push`
	- `git branch -v`
	- `git branch -r` : show all branches
		- You can pull a specific branch by checking out to the target branch
- Deleting Branches: 
	- `git branch -d <branch-name>`
		
- Publishing branches: `git push -u origin <local-branch>`

## Check Branch Info
- `git log --branches`
	- `--decorate --graph --oneline`: for better visualization
### Comparing Branches:
- `git log <branch 1>..<branch 2>`
	- `git log -p <branch 1>..<branch 2>`: list source codes too. 
- `git diff <branch 1>..<branch 2>`

## Delete Branch 
- `git branch --delete <name>`
	- or simply, `git branch -d <name>`

# Merging and Rebasing

References: 
- [ref](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- [ref2](https://www.edureka.co/blog/git-rebase-vs-merge/)
## Merge

- The first thing to understand about `git rebase` is that it solves the same problem as `git merge`. 
- Both of these commands are designed to _integrate changes from one branch into another branch_—they just do it in very different ways.
- Consider what happens when you start working on a new feature in a dedicated branch, then another team member updates the `main` branch with new commits. This results in a forked history, which should be familiar to anyone who has used Git as a collaboration tool.
- Now, let’s say that the new commits in `main` are relevant to the feature that you’re working on. To incorporate the new commits into your `feature` branch, you have two options: _merging or rebasing_.
- The easiest option is to merge the `main` branch into the feature branch using something like the following:
	- To bring the changes in the main branch, you need to switch to the target feature branch first: 

```sh
git checkout feature
git merge main
```

Or, you can condense this to a one-liner:

```sh
git merge feature main
```

- This creates a new "merge commit" in the `feature` branch that ties together the histories of both branches, giving you a branch structure that looks like this:

![img](merging.png)

- *TLDR*: _Once the two branches are merged, the feature branch cannot have the access to the latest commit of the main_
- Merging is nice because it’s a _non-destructive_ operation. The existing branches are not changed in any way. This avoids all of the potential pitfalls of rebasing (discussed below).
- On the other hand, this also means that the `feature` branch will have an extraneous merge commit every time you need to incorporate upstream changes. If `main` is very active, this can pollute your feature branch's history quite a bit. While it's possible to mitigate this issue with advanced `git log` options, it can make it hard for other developers to understand the history of the project.

#### Merge Squash

- `git merge --squah feature`: summarize all commits in the feature branch in the last commit
- `git commit -m "Two branches are merged"`

### Fast-Forward Branch
Let's say we have an issue in our application. So, we create a branch 'iss53' and work on it. Then, suddenly we receive a hotfix requiest, so we create another branch called 'hotfix'. 

![[hotfix_branch.png|700]]

We manage to fix the hotfix issue. So we merge the branch.  
```sh
git checkout master
git merge hotfix
Updating f42c576..3a0874c
Fast-forward
 index.html | 2 ++
 1 file changed, 2 insertions(+)
```

This is a **fast-forward** branch, since it has a common ancestor. 

![[fast_forward.png | 700]]

Note that the `master` branch is fast-forwarded to the `hotfix` branch.

![[basic_merge.png | 700]]

```sh
git checkout master
Switched to branch 'master'
git merge iss53
Merge made by the 'recursive' strategy.
index.html |    1 +
1 file changed, 1 insertion(+)
```


## Rebase
Let's first think about the meaning of rebase. What is the base of the feature branch? The base of the feature branch is the commit that is forked from the main branch. The meaning of the rebase is changing the base of the target branch. 

You can rebase the `feature` branch onto `main` branch using the following commands:

```sh
git checkout feature
git rebase main
```

- This moves the entire `feature` branch to begin on the tip of the `main` branch, effectively incorporating all of the new commits in `main`. But, instead of using a merge commit, rebasing _re-writes the project history_ by creating brand new commits for each commit in the original branch.

![[rebasing.png | 600]]

- *TLDR*: _Rebasing allows to the feature branch to track and use the latest commit of the main branch_
- The major benefit of rebasing is that you _get a much cleaner project history_. First, it eliminates the unnecessary merge commits required by `git merge`. Second, as you can see in the above diagram, rebasing also results in a perfectly linear project history—you can follow the tip of `feature` all the way to the beginning of the project without any forks. This makes it easier to navigate your project with commands like `git log`, `git bisect`, and `gitk`.
- But, there are _two trade-offs for this pristine commit history: safety and traceability_. If you don’t follow the [Golden Rule of Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing), re-writing project history can be potentially catastrophic for your collaboration workflow. And, less importantly, rebasing loses the context provided by a merge commit—you can’t see when upstream changes were incorporated into the feature.

If you merge the feature branch to merge
```sh
git checkout Main
git merge Feature
```

Then, git will fast-forward the Main branch to the Feature branch. 

### Conflict in Rebase
Let's say you have a Main branch and a Feature branch. 

![[rebase_conflict_1.png | 700]]
- You can see there is a conflict in line 2 of the file1.txt. 
- Let's say you want to rebase the feature branch to the Main branch.
```sh
git checkout Feature
git rebase Main
```
- Then, you will face a conflict between M1 and F1:
	- It is a sunny day! <> It is a cool day!
- Once you address the conflict, the branches would look like this:
![[rebase_conflict_2.png | 700]]
- Then, you should continue rebasing. 
	- `git rebase --continue`
- Again, you will face another conflict. You need to solve the conflict between the F1 commit and the F2 commit.
	- It is a cool day! <> It is a nice day!
- You need to repeat the above process until all conflicts are addressed.
	- Conflicts: F1<>F2, F2<>F3
- Once you finished addressing them, you will get a single line of commit histories. 
### The Golden Rule of Rebasing

Once you understand what rebasing is, the most important thing to learn is when _not_ to do it. The golden rule of `git rebase` is to never use it on _public_ branches.

For example, think about what would happen if you rebased `main` onto your `feature` branch:

![[rebase_main_branch.png|650]]

The rebase moves all of the commits in `main` onto the tip of `feature`. The problem is that this only happened in _your_ repository. All of the other developers are still working with the original `main`. Since rebasing results in brand new commits, Git will think that your `main` branch’s history has diverged from everybody else’s.

The only way to synchronize the two `main` branches is to merge them back together, resulting in an extra merge commit _and_ two sets of commits that contain the same changes (the original ones, and the ones from your rebased branch). Needless to say, this is a very confusing situation.

So, before you run `git rebase`, always ask yourself, “Is anyone else looking at this branch?” If the answer is yes, take your hands off the keyboard and start thinking about a non-destructive way to make your changes (e.g., the `git revert` command). Otherwise, you’re safe to re-write history as much as you like.
