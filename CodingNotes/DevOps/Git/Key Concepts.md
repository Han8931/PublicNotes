---
tags:git
---
# Introduction to Git 
## Git: Global Information tracker
What is _version control_, and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

## Centralized Version Control Systems
People often encounter a situation that they need to collaborate with developers on other systems. To deal with this problem, Centralized Version Control Systems (CVCSs) were developed. These systems (such as CVS, Subversion, and Perforce) have a single server that contains all the versioned files, and a number of clients that check out files from that central place. For many years, this has been the standard for version control.

This setup offers many advantages, especially over local VCSs. For example, everyone knows to a certain degree what everyone else on the project is doing. Administrators have fine-grained control over who can do what, and it’s far easier to administer a CVCS than it is to deal with local databases on every client.

However, this setup also has some serious downsides. The most obvious is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they’re working on. If the hard disk the central database is on becomes corrupted, and proper backups haven’t been kept, you lose absolutely everything — the entire history of the project except whatever single snapshots people happen to have on their local machines. Local VCSs suffer from this same problem — whenever you have the entire history of the project in a single place, you risk losing everything.

## Distributed Version Control Systems
This is where Distributed Version Control Systems (DVCSs) step in. In a DVCS (such as Git, Mercurial, Bazaar or Darcs), clients don’t just check out the latest snapshot of the files; rather, they fully mirror the repository, including its full history. Thus, if any server dies, and these systems were collaborating via that server, any of the client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data.

# What is Git?
The major difference between Git and any other VCS (Subversion and friends included) is the way Git thinks about its data. Conceptually, most other systems store information as a list of file-based changes. These other systems (CVS, Subversion, Perforce, Bazaar, and so on) think of the information they store as a set of files and the changes made to each file over time (this is commonly described as delta-based version control).

Git doesn’t think of or store its data this way. Instead, Git thinks of its data more like a series of snapshots of a miniature filesystem. With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a **stream of snapshots**.

## Nearly Every Operation Is Local

## Integrity
Everything in Git is checksummed before it is stored and is then referred to by that checksum. This means it’s impossible to change the contents of any file or directory without Git knowing about it. This functionality is built into Git at the lowest levels and is integral to its philosophy. You can’t lose information in transit or get file corruption without Git being able to detect it.

The mechanism that Git uses for this checksumming is called a **SHA-1 hash**. This is a 40-character string composed of hexadecimal characters (0–9 and a–f) and calculated based on the contents of a file or directory structure in Git. A SHA-1 hash looks something like this:

# Three States

- Modified means that you have changed the file but have not committed it to your database yet.
- Staged means that you have marked a modified file in its current version to go into your next commit snapshot.
- Committed means that the data is safely stored in your local database.

The basic Git workflow goes something like this:
1. You modify files in your _working tree (working dir)_.
2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the _staging area_.
3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your _Git directory_.

### working area
- The working area, in brief, is the files that are not in the staging area. 
- They're _not handled by Git_. They're kind of just in your local directory. They can also be called _untracked files_. The working area is like your scratch space, it's where you can add new content, you can modify delete content, if the content that you modify or delete is in your repository you don't have to worry about losing your work.

### Staging area
- The staging area, that's what _files are going to be a part of your next commit_. It's how Git knows what is going to change between the current commit and the next one. We're gonna deep-dive into the staging area in the next section. Briefly, the repository, that's the files that Git actually knows about.

### Repository
- The _repository contains all of your commits_. And the _commit is a snapshot_ of what your working and staging area look like at the time of the commit. It's in your .git directory. And that's all of the files in your repository, they're stored away safely, you can continue to make changes as you work and you can always check out a fresh copy if you need one.

So very, very important, the staging area. That's how Git knows what's gonna change between your current commit and your next commit.  
Nina: A clean staging area, people think it's empty, but that's not really the case. _A clean staging area isn't empty._

Actually, what's going on is _the baseline staging area is a copy of your latest commit_. So it contains a list of files that were in your last commit. The way that Git stores this information, the index is actually a binary file in the .git directory.

Don't try to open it you'll just, get a bunch of yucky data. When you add, remove, rename files to the staging area, Git knows it.

In order to look at our index, We use the plumbing command `git ls-files` with the `-s` flag.  

If you want to add a file to the next commit, git add, file name. If you want to delete a file in the next commit, git rm. A lot of people, in their workflows, tend to remove the file from their working area, and then they have to stage it in a separate step, and it's kind of annoying.

So you can just tell Git to remove the file directly, and it'll do that in one step, `git rm`. If you wanna rename a file, that's going to be part of your next commit, you can just use the `git mv` command, mv for move.  

When you unstage files from the staging area, remember you're not removing the files. The staging area isn't empty. What you're doing is you're just replacing them with a copy that's currently in a repository.  
So a little bit of how content moves in Git. We can use that git connect-a to move straight from the working area to the repository.

We add files from the working area to the staging area, we commit from the staging area to the repository. And we check out from from the repository to the staging area and the working area.


