---
tags:bash, terminal, linux, command
---

## Basics
- Piping (`|`): Send the standard output of a command to the standard input of another command, use the pipe character `|`. 

## Commands
- Shell globbing: The glob character `*` tells the shell to match any number of arbitrary characters.
- `cd` : change directory
	- `cd ;` : change directory to the previous dir
- Redirection:
	- Output redirection:
		- `>`: overwrite (redirect standard output)
		- `>>`: append
	- (Standard) Input redirection:
		- `<` : e.g.,  `wc -w hello.txt`
		- `<<` : _here document_. e.g., `cat << EOF >> output.txt`, and close it by typing `EOF`
			- This command takes multiple texts and redirect them to `output.txt`
		- `<<<` : _here string_ takes a string 
			- `wc -w <<< "I wanna go swimming"`
			- Double quotes are important
	- Standard error redirection:
		- `2>` : `ls /ffffff > f.txt 2> error.txt`
		- `ls /ffffff > f.txt 2>&1` : send both the standard output and error to `f.txt`
- `mkdir -p <path>`:  makes any missing parent directories as needed. 
- `cat -n <file>`: show numbers of all lines
	- `-b`: show numbers of all non-empty lines
- `more <file>`: displays a text file but stops after it displays each page of data. 
	- `less` command is more advanced
- `wc` (word count): print number of lines, words, and bytes 
	- `ls -l | wc`
	- `ls -l | wc -l`: print only line numbers
	- `wc < hello.txt`
- `uniq` (unique): report duplicate values
	- `uniq -d`: only print duplicate lines
	- `uniq -u`: only print unique lines
	- `uniq -c`: prefix lines by the number of occurrences
	- `sort foo.txt | uniq -c | sort -nr`
		- `sort -nr`: sort by number and reverse it
- `echo`: 
	- `echo *` : print a list of files in the current dir. 
	- `echo $USER`
	- `echo $PATH`
	- `echo \*`: show all files in a current dir
		- ?: match with a single character. ex) echo files.???
	- `echo {a,b,c}.txt`: echo every combination consists of a,b,c
		- {}: curly braces, e.g., {1..50} / {a,b,c}
		- `echo app.{js,html,css,py}`
		- `touch app.{js,html,css,py}`
		- `echo F*` : echo files match with F\*
- `diff`: 
	  - `diff file1.txt file2.txt`
	  - ex) 24a25: 24th line of the first file is appended at the 25th line of hte second file
	  - ex) 24c25: 24th line of the first file is changed at the 25th line of hte second file
	  - `-u` or `-y` are commonly used

## Search

- `find`: find files or dirs
	- First need to provide a location to look inside
	- Then, provide name to search
	   - ex) `find . -name '\*.js'` : nested search
	- To search with a partial name: `find . -name '\*7\*'`
	- Specific type: `find . -type d/f -name '\*7\*'`
	- or / and: `find . -type d/f -name '\*7\*' -or/and -name 'file'`
	- Search by file size/ modifed time: 
	   - -size +100k: more than 100kb
	   - -size +100k -size -1M: more than 100kb and less than 1M
	   - -mtime +3: modified more than 3 days ago
	 - -exec: execute a command on each result of the search
		 - `find . type -f -exec at {} \\; `: backslach with semicolon is the command ends and the curly braces are the place holder
	 - `find . -name "*.tex" -o -name "*.sty" | entr make`
	 - `find ./cls_task/checkpoint/ -name noise_bert*_grad* -exec stat -c "%n %y" {} \;`
- `grep` (global regular expression print): The grep command prints the lines from a file or input stream that match an expression.
	- `grep <key> files.py` : vanilla search
	- `grep -n <key> files.py`: show line numbers
	- `grep -nC 2 key files.py`: show line numbers and num lines of output context (before and after results). 
	- `grep -r "chicken" .` : search recursively in all files
	- `-i` : case insensitive
	- `-v` : inverts the search, prints all lines that don't match



## Disk / Files

- `du`: shows the disk usage for a specific directory (by default, the current directory) in a human-readable form.
	- -h/m/g: output in human readable format, mega ,or giga bytes 
	- `du - h | sort -h | tail`
	- `du -h Documents`: find located file
	- By default, the du command displays all the files, directories, and subdirectories under the current directory, and it shows how many disk blocks each file or directory takes. 
	- You can use `ls -sh` instead to see the file size. 
	- Check my disk usage 
		- `du -sh /home/han`
		- `sudo du -h --max-depth=1`
	- Check all users:
		- `du -shc /data/*`
 
- `df`: mounted space information. It is easy to see when a disk is running out of space.

- `history`: 
	- `history | grep 'echo $PATH'`
	- `history | grep 'sudo pacman -S app'`
	- You can recall the last command by `!!`
	- Also, you can recall any command from the history list by typing like `!42`.
## Process
- `ps`: process status
	- `ps axww | grep "vlc"`
	- `ps x` : show all of your running processes
	- `ps ax` : show all processes on the system, not just the ones you won
	- `ps u` : Include more detailed info on processes
	- `ps aux` : combine the above options
	- `ps u $$` : Inspect the current shell process
- `kill`:
	- `kill -15 <pid>` (gentle kill) then `kill -9 PID`  (force quitting)
	- `kill -STOP <pid>` : Freeze a process instead of terminating
	- `kill -CONT <pid>` : Continue running the process again
- `jobs` / `bg` / `fg`:
	- `jobs`: check job status
		- ex) Check stopped jobs
		- `&` at the end of the command means a job is running in the background
	- `fg`: We can resume the process by using `fg` with the job number 
		- `fg 2`
	- `bg`: 
		- Normally, when you run a Unix command from the shell, you don't get the shell prompt back until the program finished executing. However, you can detach a process from the shell and put it in the "background" with the ampersand. 
		- Just put `&` at the end of the command to run it in the background
			- `gunzip file.gz &`
		- or to run a stopped process in bkg, use `bg 1`
		- `nohup` : send process to the background
		- The dark side of running background processes is that they may expect to work with the standard input. Thus, the best way to make sure to redirect its output. 
## Archive

- `gzip` (gunzip): compression command (\*.gz)
	- `gzip target`: this will only keep the compressed file
	- `gzip -k target`: this will keep (-k) the original file too
	- `gzip -kv target`: also shows a compression efficiency
	- `gzip -d target`: decompress
	- gunzip:
- `tar`: create an archive, grouping multiple files in a single file (contrast to gzip)
	- `tar -cf archive.tar file1 file2`: -c: create -f: filename
		- This does not really compress files
		- We can zip this file by `gzip -k archive.tar`
	- `tar -tf archive.tar`: view inside the archive before extracting files
	- `tar -xf archive.tar`: extract files from an archive
		- To extract zipped archive we need to run `gzip -d` first.
		- `-x` : extract files
	- To create / extract a zipped archive:
		- `tar -czf archive.tar.gz file1 file2`
		- `tar -xzf archive.tar.gz`
	- Additionally, we can put `-v` for the verbose operation
	- xargs: convert input from standrad input into arguments to a command
		- `cat text_file_of_args.txt | rm`: this doesn't work since rm has to put args after it. A simple solution is....
		- `cat text_file_of_args.txt | xargs rm`

## Symbolic Link

- `ln`: create links
	- Hard links: ex) `ln target.txt linkname.txt`
		- If the original file is removed, hardlink will be still there.
	- Symbolic links: ex) `ln -s target.txt linkname.txt`
		- If the original file is removed, symlink will be there too, but we cannot open the link.
		- `ls -l /usr/bin/python*` : we can see some symlinks
	- Create symbolic links recursively:
		- `cp -rs <absolute source path> <absolute destination link path>`

## Permission

- `ls -al`:
 ```
[ File type ][ Owner permissions ][ Group permissions ][ Everyone permissions ]
```
The characters can be one of four options:
```
r = read permission
w = write permission
x = execute permission
- = no permission
```

- `useradd [user]`: create an user
- `userdel [user]`: delete an user
	- `userdel -r [user]`: delete an user's directory too
- `who`: displays the users logged in to the system
	- whoami : tells me who am i?
- `su [user]`: while you are logged in to the terminal shell with one user, you might have the need to switch to another user. 
	- Without username, it logs in as root user.
	- `su -l [user]` : login as user. You’ll need to enter a password for that user.
	- `su - [user]` : Starts a new login shell as another username specified. 
	- `su –c [command]`: Runs a specific command as the specified user.
- `sudo -iu <username>` logs you in as `<username>`, without having to know `<username>`'s password.
- `passwd`: change password 
	- `sudo passwd elvis` : change elvis's password
	- If you ever need to do a mass password change for lots of users on the system, the `chpasswd` command can be a lifesaver.
- `chown <user>:<group> dir` : change owner
	- `sudo chown han Music/`
	- `sudo chown -R han Music/` : recursively change ownership
	- owner / group owner : we can check this by typing `ls -l`
	- Change group owner:
		- check group first by `groups`
		- `sudo chown han:groupname Music/`
- `chmod` : owner/ group / world (everyone else other than owner and group)
		- r,w,x,-  : file can be read, modified, executed, and file cannot be read, modified, or executed
		- `chmod mode file`
			- `u/g/o/a` : user(owner) / group / others (world) / all
			- `s` to set the SUID or SGID on execution 
			- `t` to set the sticky bit
		- `chmod g+w file.txt` : add writing permission to the group
		- `chmod g-w file.txt` : remove writing permission from the group
		- `chmod a=r file.txt` : set permissions to read only for all.
		- `chmod ug+rw test.txt`
		- the mode can represented as binary numbers 
			- rwx: 111 (7) / r--: 100 (4) / r-x: 101 (5)
			- `chmod 760 newfile`
		- `chmod -R MODE DIRECTORY`: change file permission recursively

## ETC

- `tr`: Translate characters into other characters
	- replace standard inputs and write them into standard outputs
- `tee` : Copy a file and print it on standard output, simultaneously.
- `tree` : show tree structure of directories
  
  
  

  
  
 
 
  
  
