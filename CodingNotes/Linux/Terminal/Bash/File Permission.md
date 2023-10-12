---
tags:bash, terminal, linux, command, file permission
---

# Understanding Linux File Permissions

## The /etc/passwd file 
The Linux system uses a special file to match the login name to a corresponding UID value. This file is the `/etc/passwd` file. The `/etc/passwd` file contains several pieces of information about the user.

The list can be very long, so we've truncated the file from our system. 
- The `root` user account is the administrator for the Linux system and is always assigned UID (user ID) 0. 
- As you can see, the Linux system creates lots of user accounts for various functions that aren't actual users. These are called **system accounts**. A system account is a special account that services running on the system use to gain access to resources on the system. All services that run in background mode need to be logged into the Linux system under a system user account.

`rich:x:500:500:Rich Blum:/home/rich:/bin/bash `
The fields of the /etc/passwd file contain the following information:
- The login username
- The password for the user
- The numerical UID of the user account
- The numerical group ID (GID) of the user's primary group
- A text description of the user account (called the comment field)
- The location of the $HOME directory for the user
- The default shell for the user
The password field in the /etc/passwd file is set to an x.  Now, most Linux systems hold user passwords in a separate file (called the _shadow_ file, located at `/etc/shadow`). Only special programs (such as the login program) are allowed access to this file.

As you can see, the `/etc/passwd` file is a standard text file. You can use any text editor to manually perform user management functions (such as adding, modifying, or removing user accounts) directly in the `/etc/passwd` file. However, this is an extremely dangerous practice. If the `/etc/passwd` file becomes corrupted, the system won't be able to read it, and it will prevent anyone (even the root user) from logging in. Instead, it's safer to use the standard Linux user management utilities to perform all user management functions.

## The /etc/shadow file

The `/etc/shadow` file provides more control over how the Linux system manages passwords. Only the root user has access to the `/etc/shadow` file, making it more secure than the `/etc/passwd` file.

## User Management

### Adding a new user
The primary tool used to add new users to your Linux system is `useradd` . This command provides an easy way to create a new user account and set up the user's `$HOME` directory structure all at once. The command uses a combination of system default values and command-line parameters to define a user account. To see the system default values used on your Linux distribution, enter the `useradd` command with the `-D` parameter.

The `-D` parameter shows what defaults the `useradd` command uses if you don't specify them in the command line when creating a new user account. This example shows the following default values:

- The new user will be added to a common group with group ID 100.
- The new user will have a HOME account created in the directory `/home/loginname`.
- The account will not be disabled when the password expires.
- The new account will not be set to expire at a set date.
- The new account will use the bash shell as the default shell.
- The system will copy the contents of the `/etc/skel` directory to the user's `$HOME` directory.

The useradd command allows an administrator to create a default `$HOME` directory configuration and then uses that as a template to create the new user's `$HOME` directory. This allows you to place default files for the system in every new user's `$HOME` directory automatically. 

### Removing a user
If you want to remove a user from the system, the userdel command is what you need. By default, the `userdel` command removes only the user information from the `/etc/passwd` and `/etc/shadow` files. It doesn't remove any files the account owns on the system. If you use the `-r` parameter, userdel will remove the user's `$HOME` directory, along with the user's mail directory.

### Modifying a user

The `usermod` command is the most robust of the user account modification utilities. It provides options for changing most of the fields in the `/etc/passwd` file.
- `-l` to change the login name of the user account
- `-L` to lock the account so the user can't log in
- `-p` to change the password for the account
- `-U` to unlock the account so that the user can log in

### Create Home directory for existing users in Linux
To create a home directory for an existing user, use the `usermod` command with the `-m` (move) and `-d` (directory) options.
- `sudo usermod -m -d /home/new_directory username`

## Using Linux Groups

User accounts are great for controlling security for individual users, but they aren't so good at allowing groups of users to share resources. To accomplish this, the Linux system uses another security concept, called **groups**.

Group permissions allow multiple users to share a common set of permissions for an object on the system, such as a file, directory, or device (more on that later in the “Decoding File Permissions” section).

Each group has a unique GID, which, like UIDs, is a unique numerical value on the system. Along with the GID, each group has a unique group name. There are a few group utilities you can use to create and manage your own groups on the Linux system. This section discusses how group information is stored and how to use the group utilities to create new groups and modify existing groups.

### The /etc/group file
Just like user accounts, group information is stored in a file on the system. The /etc/group file contains information about each group used on the system.

Since the `/etc/group` file is a standard text file, you can manually edit the file to add and modify group memberships. However, be careful that you don't make any typos or you could corrupt the file and cause problems for your system. Instead, it's safer to use the `usermod` command (discussed earlier in the “Exploring Linux Security” section) to add a user account to a group. Before you can add users to different groups, you must create the groups.

### Creating new groups
The groupadd command allows you to create new groups on your system:
- `sudo groupadd <name>`
- `sudo groupdel <name>`
- `groupmod -n sharing shared`: change the name of group

### Add Users
- `sudo usermod -G demo user`

## Sharing Files
- **The set user ID (SUID)**: When a file is executed by a user, the program runs under the permissions of the file owner. It can be set as follows:
```sh
chmod u+s file.txt
```

Also, it can be removed by
```sh
chmod u-s test.txt
```

When the SUID bit is set on an executable file, this means that the file will be executed with the same permissions as the owner of the executable file. Let’s take a practical example. If you look at the binary executable file of the passwd command, it has the SUID bit set.

```
linuxhandbook:~$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 59640 Mar 22  2019 /usr/bin/passwd
```

This means that any user running the passwd command will be running it with the same permission as root.

- **The set group ID (SGID)**: For a file, the program runs under the permissions of the file group. For a directory, new files created in the directory use the directory group as the default group.
- **The sticky bit**: When applied to a directory, only file owners can delete or rename the files in the directory.

The SGID bit is important for sharing files. By enabling the SGID bit, you can force all new files created in a shared directory to be owned by the directory's group and now the individual user's group.


## Access Control Lists

Linux developers have devised a more advanced method of file and directory security called an access control list (_ACL_). The ACL allows you to _specify a list of multiple user or groups, and the permissions that are assigned to them_. Just like the basic security method, ACL permissions use the same read, write, and execute permission bits but can now be assigned to multiple users and groups.

To use the ACL feature in Linux, you use the `setfacl` and `getfacl` commands. The getfacl command allows you to view the ACLs assigned to a file or directory.


The `setfacl` command allows you to modify the permissions assigned to a file or directory using the `-m` option, or remove specific permissions using the `-x` option. You define the rule with three formats:
- u:uid:perms
- g:gid:perms 
- o::perms

