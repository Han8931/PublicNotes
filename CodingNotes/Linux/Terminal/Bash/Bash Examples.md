# For Loops

## Changing the field separator

The cause of this problem is the special environment variable _IFS_ , the _internal field separator_. The IFS environment variable defines a list of characters the Bash shell uses as field separators. By default, the Bash shell considers the following characters as field separators:
- A space
- A tab
- A newline

If the Bash shell sees any of these characters in the data, it assumes that you're starting a new data field in the list. When working with data that can contain spaces (such as filenames), this can be annoying, as you saw in the previous script example.

To solve this problem, you can temporarily change the IFS environment variable values in your shell script to restrict the characters the Bash shell recognizes as field separators. For example, if you want to change the IFS value to recognize only the newline character, you need to do this:
```sh
IFS=$'\n'
```
Adding this statement to your script tells the Bash shell to ignore spaces and tabs in data values. 

> **Note**: When working on long scripts, you may change the `IFS` value in one place and then forget about it and assume the default value elsewhere in the script. A safe practice to get into is to save the original `IFS` value before changing it and then restore it when you're finished. This technique can be coded like this:
```sh
IFS.OLD=$IFS 
IFS=$'\n' 
...
IFS=$IFS.OLD
```
>This ensures that the `IFS` value is returned to the default value for future operations within the script.

Other excellent applications of the `IFS` environment variable are possible. Suppose you want to iterate through values in a file that are separated by a colon (such as in the `/etc/passwd` file). You just need to set the IFS value to a colon:
```sh
IFS=:
```
If you want to _specify more than one IFS character_, just string them together on the assignment line:
```
IFS=$'\n':;"
``` 
This assignment uses the newline, colon, semicolon, and double quotation mark characters as field separators. There's no limit to how you can parse your data using the IFS characters.


## Reading a directory using wildcards

Finally, you can use the `for` command to _automatically iterate through a directory of files_. To do this, _you must use a wildcard character in the file or pathname_. This forces the shell to use **_file globbing_**. File globbing is the process of producing filenames or pathnames that match a specified wildcard character. 

This feature is great for processing files in a directory when you don't know all the filenames:
```sh
#!/bin/bash 
 # iterate through all the files in a directory 
  
 for file in /home/rich/test/* 
 do 
    if [ -d "$file" ] 
    then 
       echo "$file is a directory" 
    elif [ -f "$file" ] 
    then 
       echo "$file is a file" 
    fi 
 done 
```

> **Note**: Notice that you can enter anything in the list data. Even if the file or directory doesn't exist, the for statement attempts to process whatever you place in the list. This can be a problem when you're working with files and directories. You have no way of knowing if you're trying to iterate through a nonexistent directory. It's always a good idea to test each file or directory before trying to process it.

## Creating multiple user accounts
The goal of shell scripts is to make life easier for the system administrator. If you happen to work in an environment with lots of users, one of the most boring tasks can be creating new user accounts. Fortunately, you can use the `while` loop to make your job a little easier.

Instead of having to manually enter `useradd` commands for every new user account you need to create, you can place the new user accounts in a text file and create a simple shell script to do that work for you. The format of the text file we'll use looks like this: 
- loginname, name 

The first entry is the login name you want to use for the new user account. The second entry is the full name of the user. The two values are separated by a comma, making this a comma-separated values (CSV) file format. This is a very common file format used in spreadsheets, so you can easily create the user account list in a spreadsheet program and save it in CSV format for your shell script to read and process.

To read the file data, we're going to use a little shell scripting trick. We'll set the `IFS` separator character to a comma as the test part of the `while` statement. Then to read the individual lines, we'll use the `read` command. That looks like this:
```sh
while IFS=',' read –r userid name
```

The read command does the work of moving on to the next line of text in the CSV text file, so we don't need another loop to do that. The `while` command exits when the `read` command returns a `FALSE` value, which happens when it runs out of lines to read in the file. Tricky!

To feed the data from the file into the `while` command, you just use a redirection symbol at the end of the `while` command.

