---
tags:bash, terminal, linux, command, environment variable
---

# Environment Variable

**Shell variable**: The shell can store temporary variables, called _shell variables_, containing the values of text strings 
	- `STUFF=blah`: assign blah to the variable STUFF
	- To access this variable, `$STUFF`
	- Don't put any spaces around the `=` when assigning a variable.

**Environment variable**: it is not specific to the shell. All processes including subshells on Unix systems have environment variable storage. 

You can assign a _global_ environment variable with the shell's `export` command. If you'd like to make the `$STUFF` shell variable into an environment variable, then
		1. `STUFF=blah` 
		2. `export STUFF`
Changing a global environment variable within a child shell does not affect the variable's value in the parent shell even with the `export` command.

After you start a Bash shell (or spawn a shell script), you're allowed to create _local_ user-defined variables that are visible within your shell process. You can assign either a numeric or a string value to an environment variable by assigning the variable to a value using the equal sign:
`my_variable=Hello`
`echo $my_variable`

You can list environment variables by 
- `set`: show all global and local variables
- `printenv`: only global env variables. 
	- You can also search a specific variable `printenv HOME`
	- Similarly, `echo $HOME`
- `env`: only global env variables. 

> Note: It's extremely important that you not use spaces between the variable name, the equal sign, and the value.

## Remove Environment Variables

You can do this with the `unset` command. When referencing the environment variable in the `unset` command, remember **not to use the dollar sign**
- `unset my_variable`


## PATH Variable
When you enter an external command in the shell CLI, the shell must search the system to find the program. `PATH` is a special environment variable that contains the command path, a list of system directories that the shell searches when trying to locate a command. For e.g., when you run `ls`, the shell searches the directories listed in `PATH` for the `ls` program. 
- `echo $PATH` / `which python`

- To tell the shell to look in more places for programs, change the `PATH` environment varialbe. For example, by using this command, you can add a directory `dir` to the beginning of the path so that the shell looks in `dir` before looking in any of the other path directories:
	- `PATH=dir:$PATH`
	- Or you can append a directory name to the end of the `PATH` variable, causing the shell to look in `dir` last:
		- `PATH=$PATH:dir`
	- Changes to the PATH variable last only until you exit the system or the system reboots. The changes are not persistent.

## Locating System Environment Variables

When you start a Bash shell by logging into the Linux system, by default Bash checks several files for commands. These files are called _startup files_ or _environment files_. 

### Understanding the Login Shell Process
When you log into the Linux system, the Bash shell starts as a login shell. The login shell typically looks for five different startup files to process commands from:
- `/etc/profile`: This is the main default startup file for the Bash shell on the system. The other four startup files are specific for each user, located in the home (`$HOME`) directory, and can be customized for an individual user's requirements. 
- `$HOME/.bash_profile`
- `$HOME/.bashrc`
- `$HOME/.bash_login`
- `$HOME/.profile`

## Making Environment Variables Persistent

For global environment variables (those variables needed by all the users on a Linux system), it may be tempting to put new or modified variable settings in `/etc/profile` , but this is a bad idea. The file could be changed when your distribution is upgraded, and you would lose all the customized variable settings.

It is a better idea to create a file ending with `.sh` in the `/etc/profile.d/` directory. In that file, place all your new or modified global environment variable settings.

On most distributions, the best place to store an individual user's persistent Bash shell variables is in the `$HOME/.bashrc` file. This is true for all shell process types. However, if the `BASH_ENV` variable is set, keep in mind that unless it points to `$HOME/.bashrc` , you may need to store a user's variables for non-interactive shell types elsewhere.

### Locally

To persist our changes for the current user, we **add our _export_ command to the end of _~/.profile_**_._ If the _~/.profile_ file doesn’t exist, we should create it using the [_touch_](https://linux.die.net/man/1/touch) command:

```bash
touch ~/.profile
```

Then we can add our _export_ command to _~/.profile_.

Additionally, we need to open a new shell, or source our _~/.profile_ file to reflect the change. We’d execute:

```bash
. ~/.profile
```

Or if we’re using Bash, we could use the [_source_](https://linux.die.net/man/1/source) command:

```bash
source ~/.profile
```

We could also append our _export_ command to _~/.bash_profile_ if we’re using Bash, but our changes **won’t be reflected in other shells**, such as Zsh. 

**We shouldn’t add our _export_ command to _~/.bashrc_** because only [interactive Bash](https://www.tldp.org/LDP/abs/html/intandnonint.html) shells read this configuration file. If we open a non-interactive shell or a shell other than Bash, our _PATH_ change won’t be reflected.

### Globally

We can add a new path for all users on a Unix-like system by **creating a file ending in _.sh_ in _/etc/profile.d/_** and adding our _export_ command to this file.

For example, we can create a new script file, _/etc/profile.d/example.sh_, and add the following line to append _/some/new/path_ to the global _PATH:_

```bash
export PATH=$PATH:/some/new/path
```

All of the scripts in _/etc/profile.d/_ will be executed when a new shell initializes. Therefore, we need to open a new shell for our global changes to take effect.

We can also add our new path directly to the existing _PATH_ in the _/etc/environment_ file:

```bash
PATH=<existing_PATH>:/some/new/path
```

The _/etc/environment_ file isn’t a script file, it only contains simple variable assignments, and it’s less flexible than a script. Because of this, making _PATH_ changes in _/etc/environment_ is discouraged. We recommend adding a new script to _/etc/profile.d_ instead.




## Learning about Variable Arrays
A really cool feature of environment variables is that they can be used as arrays. An array is a variable that can hold multiple values. Values can be referenced either individually or as a whole for the entire array. 

To set multiple values for an environment variable, just list them in parentheses, with values separated by spaces:
- `mytest=(zero one two three four) `

To reference an individual array element, you must use a numerical index value, which represents its place in the array. The numeric value is enclosed in square brackets, and everything after the dollar sign is encased by curly brackets:
- `echo ${mytest[2]} `

To display an entire array variable, you use the asterisk wildcard character as the index value:
- `echo ${mytest[*]}`

You can also change the value of an individual index position:
- `mytest[2]=seven `
- `echo ${mytest[2]} `

You can even use the `unset` command to remove an individual value within the array, but be careful, because this gets tricky. Consider this example:
- `unset mytest[2] `
- `echo ${mytest[*]}`

You can remove the entire array just by using the array name in the `unset` command:
- `unset mytest `