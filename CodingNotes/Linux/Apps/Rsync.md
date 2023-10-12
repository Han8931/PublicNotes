---
tags:
  - linux
  - terminal
  - share
  - file
  - management
  - backup
  - sync
  - rsync
---
A very basic approach is to use
- `python -m http.server`
	- By default, it runs on port 8000, os if the machine you run this on is at address 10.1.2.4, point your browser on the destination system to `http://10.1.2.4:8000` and you will be able to grab what you need
	- However, this approach is not secure 

## rsync

>Rsync  finds files that need to be transferred using a "_quick check_" algorithm (by default) that _looks for files  that  have  changed  in size  or  in last-modified time_.  Any changes in the other preserved attributes (as requested by options) are  made  on  the  destination file  directly  when  the quick check indicates that the file's data does not need to be updated.

When you want to start copying more than just a file or two, you can turn to tools that require server support on the destination. For example, you can copy an entire directory structure to another place with `scp -r`, provided that the remote destination has SSH and SCP server support. 
- `scp -r directory username@remote_host[:dest_dir]`

However, this method is not very flexible. In particular, after the transfer completes, the remote host may not have an exact copy of the directory. If `directory` already exists on the remote machine and contains some extraneous files, those files persist after the transfer. 

If you expect to do this sort of thing regularly, you should use a dedicated synchronizer system that can also perform analysis and verification. On linux, `rsync` is the standard synchronizer, offering good performance and many useful ways to perform transfers. 

### Getting Started with rsync
To get `rsync` working between two hosts, you must install the `rsync` on both the source and destination, and you will need a way to access one machine from the other. 

On the surface, the `rsync` command is not much different from `scp`. In fact, you can run `rsync` with the same arguments. For example, to copy a group of files to your home directory on host, 
- `rsync file1 file2 ... user@host:`
- To transfer entire directory hierarchies, use the `-a` option. 
	- `rsync -a dir host:dest_dir` 

Copying directories can be tricky, so if you are not exactly sure what will happen when you transfer the files, use the `-nv` option combination. The `-n` option tells `rsync` to operate in "dry run" mode-- that is, to run a trial without actually copying any files.  The `-v` option is for verbose mode, which show details about the transfer and the files involved.
- `rsync -nva dir host:dest_dir`

### Making Exact Copies of a Directory Structure 

By default, `rsync` copies files and directories without considering the previous contents of the destination directory. For example, if you transferred directory `d` containing the files `a` and `b` to a machine that already had a file named `d/c`, the destination would contain `d/a`, `d/b`, and `d/c` after the `rsync`. 

To make an exact replica of the source directory, you must delete files in the destination directory that do not exist in the source directory, such as `d/c` in this example. 
- `rsync -a --delete dir host:dest_dir`

### Using the Trailing Slash

Be particularly careful when specifying a directory as the source in an `rsync` command line. Consider the following basic command:
- `rsync -a dir host:dest_dir`
Upon completion, you will have the directory `dir` inside `dest_dir` on host. 
However, adding a slash (/) to the source name significantly changes the behavior
- `rsync -a dir/ host:dest_dir`
Here, `rsync` copies everything inside `dir` to `dest_dir` on host without actually creating `dir` on the destination host. 


### Excluding Files and Directories

One important feature of `rsync` is its ability to exclude files and directories from a transfer operation. 
- `rsync -a --exclude=.git src host:`
	- Exclude all files and directories named `.git` , because `--exclude` takes a pattern, not an absolute filename
- To exclude one specific item, specify an abolute path that starts with `/`
	- `rsync -a --exclude=/src/.git srt host:`
- The following command will exclude all files with the _.txt_ extension, as well as the _dir3_ and _dir4_ directories:

```
rsync -av --exclude '*.txt' --exclude 'dir3' --exclude 'dir4' sourcedir/ destinationdir/
```

You can add as many **`--exclude`** entries as you need. To keep the command tidy, you can specify files and directories in the **`--exclude`** option using curly brackets. Separate the patterns using a comma.

For example, we can shorten the above command in this fashion:

```
rsync -av --exclude={'*.txt','dir3','dir4'} sourcedir/ destinationdir/
```

- When you need to exclude a large number of different files and directories, you can use the rsync **`--exclude-from`** flag. To do so, create a text file with the name of the files and directories you want to exclude. Then, pass the name of the file to the **`--exlude-from`** option.

The command looks like this:

```
rsync -av --exclude-from={'list.txt'} sourcedir/ destinationdir/
```

The rsync tool skips all files and directories you list in the file. You can add any pattern we used in this guide.

### Checking Transfers, Adding Safeguards, and Using Verbose Mode

To speed operation, `rsync` uses a quick check to determine whether any files on the transfer source are already on the destination. The check uses a combination of the file size and its last-modified date. The first time you transfer an entire directory hierarchy to a remote host, `rsync` sees that non of the files already exist at the destination, and it transfers everything. 
- `--update`: skip files that are newer on the receiver

### Compressing Data
`-z` option in conjunction with `-a` to compress the data before transmission, which can improve perforamance in certain situations, such as when you are uploading a large amount of data across a slow connection or when the latency between the two hosts is high. 

### Transferring Files to Your Computer
You can also transfer files from a remote machine to your local host by placing the remote host and remote source path as the first argument on the command line. For example, to transfer `src_dir` on the remote system to `dest_dir` on the local host, run this command:
- `rsync -a host:src_dir dest_dir`
