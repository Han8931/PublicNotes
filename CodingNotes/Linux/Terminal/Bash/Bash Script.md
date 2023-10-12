---
tags: linux, bash, terminal, script
---
## Basics
Bash scripts generally start with the following line, which indicates that the `/bin/sh` program should execute the commands in the script file. 
- `#!/bin/sh`
- The `#!` part is called a _shebang_.
- `#` (pound sign) character also works as a comment.
- `chmod +rx script.sh` : to make a script executable.

## Quoting and Literals

When you use quotes, you are often trying to create a _literal_, a string that the shell should not analyze (or try to change) before passing it to the command line. When writing scripts and working on the command line, remember what happens when the shell runs a command:
- Before running the command, the shell looks for variables, globs, and other substitutions and performs the sibtutions if they appear
- The shell passes the results of the substitutions to the command. 

> - In computer programming, a _literal_ is the idea of expressing a _non-changing value_ in a computer program’s source code.  
> - _String interpolation_: In [computer programming](https://en.wikipedia.org/wiki/Computer_programming "Computer programming"), **string interpolation** (or **variable interpolation**, **variable substitution**, or **variable expansion**) is the process of evaluating a [string literal](https://en.wikipedia.org/wiki/String_literal "String literal") containing one or more [placeholders](https://en.wikipedia.org/wiki/Form_(document)#Placeholders "Form (document)"), yielding a result in which the placeholders are replaced with their corresponding values.
```python
apples = 4
print("I have ${apples} apples.") # string interpolation
print("I have " + apples + " apples.") # string concatenation
print("I have %s apples.", apples) # format string
```

#### Single Quote
- Turn strings into literal
- Enclosing characters in single quotes (`'`) preserves the literal value of each character within the quotes. A single quote may not occur between single quotes, even when preceded by a backslash.

#### Double Quote
- Double quotes (") work just like single quotes, except that the shell expands any variables that appear within double quotes. 
- Enclosing characters in double quotes (`"`) preserves the literal value of all characters within the quotes, with the exception of `$`, `` ` ``, `\`,

## Special Variables
- `$0` : the name of the script. 
- `$1`, `$2`, and so on. Refer a variable
- `shift` : remove the first argument and advance the rest of the arguments so that `$2` becomes `$1`.
- `$#` : it holds number of arguments passed to a script. 
- `$@` : all of a script's arguments. 
- `$$` : the process ID of the shell.
- `$?` : the _exit code_ of the last command that the shell executed.

## Exit Codes
Every command that runs in the shell uses an _exit status_ to indicate to the shell that it's done processing. The exit status is an integer value between 0 and 255 that's passed by the command to the shell when the command finishes running. You can capture this value and use it in your scripts.

Linux provides the `$?` special variable that holds the exit status value from the last command that executed. You must view or use the `$?` variable immediately after the command you want to check. It changes values to the exit status of the last command executed by the shell:

- When the exit code is zero (0), it typically means that the program ran without a problem. 
- However, if the program has an error, it usually exits with a number other than 0 (e.g., 126 The command can't execute. 127 Command not found). 
```sh
# Try these commands
$ ls / > /dev/null # /dev/null is used to discard 
$ echo $?

$ ls /adfasdfe > /dev/null
$ echo $?

$ rgkljlkajd
$ echo $?
```

You can change that to return your own exit status code. The `exit` command allows you to specify an exit status when your script ends

```sh
#!/bin/bash 
# testing the exit status 
var1=10 
var2=30 
var3=$[ $var1 + var2 ] 
echo The answer is $var3 
exit 5 
```

When you check the exit status of the script, you'll get the value used as the parameter of the exit command:
```sh
$ ./test13 
The answer is 40 
$ echo $? 
5 
$
```

## Basic Math
- `bc` : text-based calculator
- `expr 1 + 1`: The expr command allowed the processing of equations from the command line, but it is extremely clunky.

The Bash shell includes the `expr` command to stay compatible with the Bourne shell; however, it also provides a much easier way of performing mathematical equations. In Bash, when assigning a mathematical value to a variable, you can enclose the mathematical equation using a dollar sign and square brackets (`$[ operation ]`):
```sh
$ var1=$[1 + 5] 
$ echo $var1 
```
Using brackets makes shell math much easier than with the expr comman.

```sh
var1=100 
var2=50 
var3=45 
var4=$[$var1 * ($var2 - $var3)] 
echo The final result is $var4 
```

> **The Bash shell mathematical operators support only integer arithmetic**. This is a huge limitation if you're trying to do any sort of real-world mathematical calculations.

There are several solutions for overcoming the Bash integer limitation. The most popular solution uses the built-in Bash calculator, called `bc`.

# Structured Commands

## Conditionals
```sh
#!/bin/sh

if [ $1 = hi ]; then
	echo 'The first argument was "hi"'
elif [ "$2" = "bye" ]; then
	echo 'The second argument was "bye"'
else
	echo -n 'The first argument was not "hi"--'
	echo It was '"'$1'"'
fi 
```
- The `[` character is an _actual program on a Unix system. _
	- It tests shell script conditionals. 
- This program is also known as _test_ (try `man test`).
	- The exit code is 0 if the test is true and nonzero when the test fails.
	- `if test [commands]; then`
- This is actually how the above script works:
	1. The shell runs the command after the `if` keyword and collects the exit code of that command.
	2. If the exit code is 0, the shell executes the commands that follow the `then` keyword, stopping when it reaches an `else` or `fi` keyword. 
	3. If the exit code is not 0 and there's an `else` clause, the shell runs the commands after the `else` keyword.
	4. The conditional ends at `fi`.
- Another important thing is the _semicolon_ (`;`). It's just the regular shell marker for **the end of a command**, and it is there because we put the `then` keyword on the same line. Without the semicolon, the shell passes `then` as a parameter to the `[` command, which often results in an error that isn't easy to track. You can avoid the semicolon by placing the then keyword on a separate line as follows:

```sh
if [ $1 = hi ]
then
	echo 'The first argument was "hi"'
fi 
```

### A workaround (solution) for empty parameter lists 

There's a potential problem with the conditional in the preceding example, due to a commonly overlooked scenario: `$1` could be _empty_, because the user might run the script with no parameters. If `$1` is empty, the test reads `[ = hi]`, and the `[` command will abort with an error. You can fix this by enclosing the parameter in quotes in one of two common ways:
- `if [ "$1" = hi]; then` 
- `if [ x"$1" = x"hi"]; then` : Note that `x` is used to make it interpreted as `x=xhi`

### Logical Constructs
- `&&` (and):  It only runs the second command if the first one was successful.
	- `[ condition1 ] && [ condition2 ]` e.g., `[ -d $HOME ] && [ -w $HOME/newfile ] `
- `||` (or): It only runs the second command if the first one was not successful.
	- `[ condition1 ] || [ condition2 ]`
	- We can use `-a` or `-o` instead of `&&` and `||`, for example.
```sh
#!/bin/sh
if [ "$1" = hi -o "$1" = bye ]; then
	echo 'The first argument was "hi"'
fi
```
- `!` (invert): `if [ ! "$1" = hi ]; then`


## Case

The case keyword does not execute any test commands and therefore does not evaluate exit codes. However, it can do pattern matching. 

```bash
#!/bin/sh
case $1 in
	bye) 
		echo Fine, bye.
		;;
	hi|hello)
		echo Nice to see you.
	what*)
		echo Whatever.
		;;
	*)
		echo 'Huh?'
		;;
esac
```

The shell executes this as follows:
1. The script matches `$1` against each case value demarcated with the `)` character. 
2. If a case value matches `$1`, the shell executes the commands below the case until it encounters `;;`, at which point it skips to the `esac` keyword. 
3. The conditional ends with `esac`.

- For each case value, you can match a single string or multiple string with `|`.
	- `hi|hello)` returns true if `$1` equals `hi` or `hello`. 
- We can use `*` or `?` patterns too.

## Loops

### For Loops 

```bash
#!/bin/sh
for str in one two three four; do
	echo $str
done
```
1. Sets the variable `str` to the first of the four space-delimited values following the `in` keyword (one).
2. Runs the `echo` command between the `do` and `done`
3. Goes back to the `for` line, setting `str` to the next value (two), runs the commands between do and done, and repeats the process until it's through with the values following the `in` keyword. 

#### For Loop with seq 
```sh
#!/bin/bash
for i in $(seq 1 9); do
   mv "Season$i" "S0$i"
done
```
**seq** command in Linux is used to generate numbers from _FIRST_ to _LAST_ in steps of _INCREMENT_. It is a very useful command where we had to generate list of numbers in while, for, until loop.
- seq [OPTION]... LAST
- seq [OPTION]... FIRST LAST
- seq [OPTION]... FIRST INCREMENT LAST

```bash
#!/bin/bash 
 # using a variable to hold the list 
  
 list="Alabama Alaska Arizona Arkansas Colorado" 
 list=$list" Connecticut" 
  
 for state in $list 
 do 
    echo "Have you ever visited $state?" 
 done 
```

```sh
#!/bin/bash

file="states.txt"

for state in $(cat $file) ;do 
	echo "Visit $state"
done
```

This example uses the `cat` command in the command substitution to display the contents of the file states.txt . Notice that the states.txt file includes each state on a separate line, not separated by spaces. The `for` command still iterates through the output of the `cat` command one line at a time, assuming that each state is on a separate line. However, this doesn't solve the problem of having spaces in data. If you list a state with a space in it, the for command still takes each word as a separate value. There's a reason for this, which we look at in the next section.

#### C-Style For Loop 

```sh
 #!/bin/bash 
 # testing the C-style for loop 
  
 for (( i=1; i <= 10; i++ )) 
 do 
    echo "The next number is $i" 
 done 
```


## While Loops

```bash
#!/bin/sh
FILE=/tmp/whiletest.$$; # $$: process id
echo firstline > $FILE

while tail -10 $FILE | grep -q firstline; do
	# Add lines to $FILE until tail -10 $FILE no longer prints "firstline"
	echo -n Number of lines in $FILE:' '
	wc -l $FILE | awk '{print $1}'
	echo newline >> $FILE
done

rm -f $FILE
```

### Using multiple test commands
The while command allows you to define multiple test commands on the while statement line. Only the exit status of the last test command is used to determine when the loop stops. This can cause some interesting results if you're not careful.
```sh
#!/bin/bash 
 # testing a multicommand while loop 
  
 var1=10 
  
 while echo $var1 
       [ $var1 -ge 0 ] 
 do 
    echo "This is inside the loop" 
    var1=$[ $var1 - 1 ] 
 done 
```

Pay close attention to what happened in this example. Two test commands were defined in the `while` statement:
```sh
 while echo $var1 
       [ $var1 -ge 0 ]
```
The first test simply displays the current value of the `var1` variable. The second test uses brackets to determine the value of the `var1` variable. Inside the loop, an echo statement displays a simple message, indicating that the loop was processed. Notice when you run the example how the output ends:

```sh
 This is inside the loop 
 -1 
 $
```

The `while` loop executed the `echo` statement when the `var1` variable was equal to 0 and then decreased the `var1` variable value. The test commands were then executed for the next iteration. The `echo` test command was executed, displaying the value of the `var1` variable, which is now less than 0. It's not until the shell executes the test command that the while loop terminates.

This demonstrates that in a multicommand `while` statement, all the test commands are executed in each iteration, including the last iteration when the last test command fails. Be careful of this. Another thing to be careful of is how you specify the multiple test commands. Note that each test command is on a separate line!


## Controlling the Loop

### The break command
#### Breaking out of a single loop 
When the shell executes a break command, it attempts to break out of the loop that's currently processing:

#### Breaking out of an outer loop
There may be times when you're in an inner loop but need to stop the outer loop. The `break` command includes a single command-line parameter value:
```bash
break n
```
where `n indicates` the level of the loop to break out of. By default, `n is` 1, indicating to break out of the current loop. If you set `n to` a value of 2, the break command stops the next level of the outer loop:
```sh
#!/bin/bash 
 # breaking out of an outer loop 
  
 for (( a = 1; a < 4; a++ )) 
 do 
    echo "Outer loop: $a" 
    for (( b = 1; b < 100; b++ )) 
    do 
       if [ $b -gt 4 ] 
       then 
          break 2 
       fi 
       echo "   Inner loop: $b" 
    done 
 done 
```

### The continue command
As with the break command, the continue command allows you to specify what level of loop to continue with a command-line parameter:
```sh
continue n
```

## Processing the Output of a Loop
Finally, you can either pipe or redirect the output of a loop within your shell script. You do this by adding the processing command to the end of the `done` command:
```sh
 for file in /home/rich/* 
  do 
    if [ -d "$file" ] 
    then 
       echo "$file is a directory" 
    elif 
       echo "$file is a file" 
    fi 
 done> output.txt
```
Instead of displaying the results on the monitor, the shell redirects the results of the for command to the file output.txt.

# Handling User Input

## Passing Parameters
The most basic method of passing data to your shell script is to use _command-line parameters_. Command-line parameters allow you to add data values to the command line when you execute the script:
`$ ./addem 10 30`
This example passes two command-line parameters (10 and 30) to the script addem . The script handles the command-line parameters using special variables. The following sections describe how to use command-line parameters in your Bash shell scripts.

## Reading parameters

The Bash shell assigns special variables, called _positional parameters_, to all of the command-line parameters entered. This includes the name of the script the shell is executing. The positional parameter variables are standard numbers, with `$0` being the script's name, `$1` being the first parameter, `$2` being the second parameter, and so on, up to `$9` for the ninth parameter.

```sh
#!/bin/bash 
# Using one command-line parameter 
# 
factorial=1 
for (( number = 1; number <= $1; number++ )) 
do 
     factorial=$[ $factorial * $number ] 
done 
echo The factorial of $1 is $factorial 
exit 
```
If you want to enter more command-line parameters for your script, each parameter must be separated by a space on the command line. And the shell assigns each parameter to the appropriate variable:
```sh
#!/bin/bash 
# Using two command-line parameters 
# 
product=$[ $1 * $2 ] 
echo The first parameter is $1. 
echo The second parameter is $2. 
echo The product value is $product. 
exit 
```

You can also use text strings as parameters:
```sh
#!/bin/bash 
# Using one command-line string parameter 
# 
echo Hello $1, glad to meet you. 
exit 
```

The shell passes the string value entered into the command line to the script. However, you'll have a problem if you try to do this with a _text string that contains spaces_. Remember that the parameters are separated by spaces, so the shell interpreted the space as just separating the two values. To include a space as a parameter value, you must use quotation marks.
```sh
$ ./stringparam.sh 'big world' 
```

If your script needs more than nine command-line parameters, you can continue, but the variable names change slightly. After the ninth variable, you must use braces around the variable number, such as `${10}` . Here's an example of doing that:
```sh
#!/bin/bash 
# Handling lots of command-line parameters 
# 
product=$[ ${10} * ${11} ] 
echo The tenth parameter is ${10}. 
echo The eleventh parameter is ${11}. 
echo The product value is $product. 
exit 
```

## Reading the Script Name
You can use the `$0` parameter to determine the script name the shell started from the command line. This can come in handy if you're writing a utility that has multiple functions or that produces log messages.
```sh
#!/bin/bash 
# Handling the $0 command-line parameter 
# 
echo This script name is $0. 
exit 
```

However, there is a potential problem. When using a different command to run the shell script, the command becomes entangled with the script name in the `$0` parameter:
```sh
$ ./positional0.sh 
This script name is ./positional0.sh. 
```

An additional issue occurs when the actual string passed is the full script path, and not just the script's name. In this case, the `$0` variable gets set to the full script path and name:
```sh
$ $HOME/scripts/positional0.sh 
This script name is /home/christine/scripts/positional0.sh. 
```

If you want to write a script that only uses the script's name, you'll have to do a little work in order to strip off whatever path is used to run the script or any entangled commands. Fortunately, there's a handy little command available that does just that. The `basename` command returns just the script's name without the path:
```sh
#!/bin/bash 
# Using basename with the $0 command-line parameter 
name=$(basename $0) 
echo This script name is $name. 
exit 
```

## Testing parameters

When the script assumes there is data in a parameter variable and no data is present, most likely you'll get an error message from your script. This is a poor way to write scripts. Always check your parameters to make sure the data is there before using it:
```sh
#!/bin/bash 
# Using one command-line parameter 
# 
if [ -n "$1" ] 
then 
     factorial=1 
     for (( number = 1; number <= $1; number++ )) 
     do 
          factorial=$[ $factorial * $number ] 
     done 
     echo The factorial of $1 is $factorial 
else 
     echo "You did not provide a parameter." 
fi 
exit 
```

# Using Special Parameter Variables
## Counting parameters
As you saw in the last section, you should verify command-line parameters before using them in your script. For scripts that use multiple command-line parameters, this checking can get tedious.

_Instead of testing each parameter, you can count how many parameters were entered on the command line_. The Bash shell provides a special variable for this purpose.

The `$#` variable contains the number of command-line parameters included when the script was run. You can use this special variable anywhere in the script, just like a normal variable:
```sh
#!/bin/bash 
# Counting command-line parameters 
# 
if [ $# -eq 1 ] 
then 
     fragment="parameter was" 
else 
     fragment="parameters were" 
fi 
echo $# $fragment supplied. 
exit 
```
you might think that because the `$#` variable contains the value of the number of parameters, using the variable `${$#}` would represent the last command-line parameter variable. It turns out that you can't use the dollar sign within the braces. Instead, you must replace the dollar sign with an exclamation mark. 

```bash
#!/bin/bash 
# Testing grabbing the last parameter 
# 
echo The number of parameters is $# 
echo The last parameter is ${!#} 
exit 
```

> **Note**: this only works in _bash_. So you need to run `bash lastparameter.sh 1 2 3`

## Grabbing All the Data
The `$*` and `$@` variables provide easy access to all your parameters. Both of these variables include all the command-line parameters within a single variable.

- The `$*` variable takes all the parameters supplied on the command line as **a single word**. The word contains each of the values as they appear on the command line. Basically, instead of treating the parameters as multiple objects, the `$*` variable treats them all as one parameter.
- The `$@` variable, on the other hand, takes all the parameters supplied on the command line as **separate words** in the same string. It allows you to iterate through the values, separating out each parameter supplied. This is most often accomplished using a for loop.

```bash
#!/bin/bash 
# Testing different methods for grabbing all the parameters 
# 
echo 
echo "Using the \$* method: $*" 
echo 
echo "Using the \$@ method: $@" 
echo 
exit 
```

```bash
#!/bin/bash 
# Exploring different methods for grabbing all the  parameters 

echo "Using the \$* method: $*" 
count=1 
for param in "$*" 
do 
     echo "\$* Parameter #$count = $param" 
     count=$[ $count + 1 ] 
done 
# 
echo 
echo "Using the \$@ method: $@" 
count=1 
for param in "$@" 
do 
     echo "\$@ Parameter #$count = $param" 
     count=$[ $count + 1 ] 
done 
echo 
exit 
```

## Being Shifty
Another tool you have in your Bash shell tool belt is the `shift` command. The Bash shell provides the shift command to help you manipulate command-line parameters. The shift command literally shifts the command-line parameters in their relative positions.

When you use the `shift` command, it moves each parameter variable one position to the left by default. Thus, the value for variable `$3` is moved to `$2` , the value for variable `$2` is moved to `$1` , and the value for variable `$1` is discarded (note that the value for variable `$0` , the program name, remains unchanged).

This is another great way to iterate through command-line parameters. You can just operate on the first parameter, shift the parameters over, and then operate on the first parameter again.

```bash
#!/bin/bash 
# Shifting through the parameters 
# 
echo 
echo "Using the shift method:" 
count=1 
while [ -n "$1" ] 
do 
     echo "Parameter #$count = $1" 
     count=$[ $count + 1 ] 
     shift 
done 
echo 
exit 
```

The script performs a while loop, testing the length of the first parameter's value. When the first parameter's length is 0, the loop ends. After testing the first parameter, the shift command is used to shift all the parameters one position.

> **Note**: Be careful when working with the shift command. When a parameter is shifted out, its value is lost and can't be recovered.

```bash
#!/bin/bash 
# Shifting multiple positions through the parameters 
# 
echo 
echo "The original parameters: $*" 
echo "Now shifting 2..." 
shift 2 
echo "Here's the new first parameter: $1" 
echo 
exit 
```

## Working with Options

### Finding your options
On the surface, there's nothing all that special about command-line options. They appear on the command line immediately after the script name, just the same as command-line parameters. In fact, if you want, you can process command-line options the same way you process command-line parameters.

### Processing simple options

You can use the `shift` command to process command-line options.
```bash
#!/bin/bash 
# Extract command-line options 
# 
echo 
while [ -n "$1" ] 
do 
     case "$1" in 
          -a) echo "Found the -a option" ;; 
          -b) echo "Found the -b option" ;; 
          -c) echo "Found the -c option" ;; 
          *) echo "$1 is not an option" ;; 
     esac 
     shift 
done 
echo 
exit 
```





# Miscellaneous

## Command Substitution

The bash can redirect a command's standard output back to the shell's own command line. That is, you can use a command's output as an argument to another command, or you can store the command output in a shell variable by enclosing a command in `$()`.
```sh
#!/bin/sh
FLAGS=$(grep ^flags /proc/cpuinfo | sed 's/.*://' | head -1)
echo Your processor supports:
for f in $FLAGS; do
	case $f in 
		fpu) MSG="floating point unit" 
			;;
		3dnow) MSG="#3DNOW graphics extensions" 
			;; 
		mttr) MSG="memory type range register" 
			;; 
		**) MSG="unknown" 
			;; 
   esac
   echo $f: $MSG
done
```

## Temporary File Management

It's sometimes necessary to create a temporary file to collect output for use by a later command. When creating such a file, make sure that the filename is distinct enough that no other programs will accidentally write to it. Sometimes using something as simple as the shell's PID (`$$`) in a filename works, but when you need to be certain that there will be no conflicts, a utility such as `mktemp` is often a better option.
```sh
#!/bin/sh
TMPFILE1=$(mktemp /tmp/im1.XXXXXX) # The number of X can be arbitrary
TMPFILE2=$(mktemp /tmp/im2.XXXXXX)

cat /proc/interrupts > $TMPFILE1
sleep 2
cat /proc/interrupts > $TMPFILE2
diff $TMPFILE1 $TMPFILE2 
rm -f $TMPFILE1 $TMPFILE2
```
The argument to `mktemp` is a template. The `mktemp` command converts the `XXXXXX` to a unique set of characters and creates an empty file with that name. Notice that this script uses variable names to store the filename so that you only have to change on line if you want to change a filename. 

A common problem with scripts that employ temporary files is that if the script is aborted, the temporary files could be left behind. In the preceding example, pressing `CTRL-C` before the second cat leaves a temporary file in `/tmp`. Avoid this if possible. Instead, use the `trap` command to create a signal handler to catch the signal that `CTRL-C` generates and remove the temporary files, as in this handler:
```sh
#!/bin/sh
TMPFILE1=$(mktemp /tmp/im1.XXXXXX) # The number of X can be arbitrary
TMPFILE2=$(mktemp /tmp/im2.XXXXXX)
trap "rm -f $TMPFILE1 $TMPFILE2; exit 1" INT
.....
```
You must use `exit` in the handler to explicitly end script execution, or the shell will continue running as usual after running the signal handler. 

## Here Documents

Say you want to print a large section of text or feed a lot of text to another command. Rather than using several `echo` commands, you can use the shell's `here document` feature, as shown in the following script:
```sh
#!/bin/sh
DATE=$(date)
cat << EOF # <<EOF is the heare document
Date: $DATE

The output above is from the Unix date command.
It's not a very interesting command.
EOF
```
`<<EOF` tells the shell to redirect all subsequent lines to the standard input of the command that precedes `<<EOF`, which in this case is `cat`. The redirection stops as soon as the `EOF` marker occurs on a line by itself. The output of the script is
```sh
Date: $DATE

The output above is from the Unix date command.
It's not a very interesting command.
```

The marker can actually be any string, but remember to use the same marker at the beginning and end of the here document. Also, convention dictates that the marker be in all uppercase letters. 

## Important Shell Script Utilities

### basename

If you need to strip the extension from a filename or get rid of the directories in a full pathname, use the `basename` command. 
- `basename example.html .html` 
- `basename /usr/local/bin/example`
	- In both cases, it returns `example`
	- The first command strips the `.html` suffix
	- The second removes directories from the full path
```sh
#!/bin/sh
for file in *.gif; do
	# exit if there are no files 
	if [ ! -f $file ]; then
		exit
	fi
	b=$(basename $file .gif)
	echo Converting $b.gif to $b.png...
	giftopnm $b.gif | pnmtopng > $b.png
done
```

### awk

The `awk` command is not a simple single-purpose command; it's actually a powerful programming language (You can learn awk programming language). Unfortunately, `awk` usage is not something of a lost art, having been replaced by larger laguages such as Python.  Many people use `awk` only to do one thing -- to pick a single field out of an input stream like this:
- `ls -l | awk '{print $5}' `

```
1) Amit     Physics   80
2) Rahul    Maths     90
3) Shyam    Biology   87
4) Kedar    English   85
5) Hari     History   89
```

- Print only certain columns
	- `awk '{print $3 "\t" $4}' marks.txt` : seperate by tab
 - To select the fifth line of the field,
	- `awk 'FNR == 5 {print $3}'` : seperate by tab
- `docker ps | awk 'FNR==2 {print $1}' | xargs -l docker stop`

### sed

The sed ("stream editor") program is an automatix text editor that takes an input stream, alters it according to some expression, and prints the results to standard output. 
- `sed 3,6d /etc/passwd` : reads `/etc/passwd`, delete (`d`) lines three (`3`) through six (`6`), and sends the result to the standard output.

### xargs

When you have to run one command on a huge number of files, the command or shell may respond that it can't fit all of the arguments in its buffer.  Use`xargs` to get around this problem by running a command on each file name in its standard input stream. 
- `ls | xargs cat`
- `find . -name "*.txt" -type f | xargs mv -t temp_dir`
	- Find all files in the current directory with `.txt` suffix and move them to the target directory `temp_dir`
- `find . -name "*.c" | xargs rm`

### expr

If you need to use arithmetic operations in your shell scripts, the `expr` command can help. 
- `expr 1+2` : prints `3`

### exec

Replaces the current shell process with the program you name after `exec`. 

## Subshells

Say you need to alter the environment in a shell slightly but don't want a permanent change. You can change and restore a part of the environment using shell variables, but that's a clumsy way to go about things. The simple option is to use a `subshell`, an entirely new shell process that you can create just to run a command or two. 

You can think of it as a parenthesis in math equation, which makes us to compute it first. 


## Including Other Files in Scripts

## Reading User Input 
The `read` command reads a line of text from the standard input and stores the text in a variable. 
- `read var`

A no-argument call of `read` fetches a single line from the standard input stream and assigns it to the `REPLY` built-in variable:

```bash
$ read
baeldung is a cool tech site # what we type
$ echo $REPLY
baeldung is a cool tech site
```

By default the `read` command splits the input into words, considering the space, tab and newline characters as word delimiters.

```
$ read input1 input2 input3
baeldung \ # what 
is a cool \ # we 
tech site   # type
$ echo "[$input1] [$input2] [$input3]"
[baeldung] [is] [a cool tech site]
```

Let’s take a closer look at this example. We used `\` to escape _newline_ characters on each line (2 and 3) except for line 4.



## References
- How Linux Works, 2021 
- Linux Command Line and Shell Scripting Bible, 2021