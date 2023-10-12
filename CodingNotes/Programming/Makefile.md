[Reference](https://makefiletutorial.com/)

## Makefile Syntax

A Makefile consists of a set of _rules_. A rule generally looks like this:
```
targets: dependencies 
	action
	action
	action
```

```
blah: blah.o
	cc blah.o -o blah # Runs third

blah.o: blah.c
	cc -c blah.c -o blah.o # Runs second

# Typically blah.c would already exist, but I want to limit any additional required files
blah.c:
	echo "int main() { return 0; }" > blah.c # Runs first
```

The above Makefile ultimately runs all three targets. When you run `make` in the terminal, it will build a program called `blah` in a series of steps:
- Make selects the target `blah`, because the first target is the default target
- `blah` requires `blah.o`, so make searches for the `blah.o` target
- `blah.o` requires `blah.c`, so make searches for the `blah.c` target
- `blah.c` has no dependencies, so the `echo` command is run
- The `cc -c` command is then run, because all of the `blah.o` dependencies are finished
- The top `cc` command is run, because all the `blah` dependencies are finished
- That's it: `blah` is a compiled c program

For example, you can create a file **with clean command** as shown below.
```
somefile:  
	touch somefile  
clean:  
	rm -f somefile
```

### PHONY

A phony target is one that is not really the name of a file; rather it is just a name for a recipe to be executed when you make an explicit request. There are two reasons to use a phony target: to avoid a conflict with a file of the same name, and to improve performance.

If you write a rule whose recipe will not create the target file, the recipe will be executed every time the target comes up for remaking. Here is an example:

```
clean:
	rm *.o temp
```
Because the `rm` command does not create a file named clean, probably no such file will ever exist. Therefore, the `rm` command will be executed every time you say ‘make clean’.

In this example, the clean target will not work properly if a file named clean is ever created in this directory. Since it has no prerequisites, clean would always be considered up to date and its recipe would not be executed. To avoid this problem you can explicitly declare the target to be phony by making it a prerequisite of the special target `.PHONY` (see [Special Built-in Target Names](https://www.gnu.org/software/make/manual/html_node/Special-Targets.html)) as follows:

```
.PHONY: clean
clean:
        rm *.o temp
```

Once this is done, ‘make clean’ will run the recipe regardless of whether there is a file named clean.

Prerequisites of `.PHONY` are always interpreted as literal target names, never as patterns (even if they contain ‘%’ characters). To always rebuild a pattern rule consider using a “force target” (see [Rules without Recipes or Prerequisites](https://www.gnu.org/software/make/manual/html_node/Force-Targets.html)).

### Variables

Variables can only be strings. You'll typically want to use `:=`, but `=` also works. 
```
files := file1 file2
some_file: $(files)
	echo "Look at this variable: " $(files)
	touch some_file

file1:
	touch file1
file2:
	touch file2

clean:
	rm -f file1 file2 some_file
```

Single or double quotes have no meaning to Make. They are simply characters that are assigned to the variable. Quotes are useful to shell/bash, though, and you need them in commands like `printf`. In this example, the two commands behave the same:

```
a := one two # a is set to the string "one two"
b := 'one two' # Not recommended. b is set to the string "'one two'"
all:
	printf '$a'
	printf $b
```

Reference variables using either `${}` or `$()`
```
x := dude

all:
	echo $(x)
	echo ${x}

	# Bad practice, but works
	echo $x 
```

### Targets
#### The all target

Making multiple targets and you want all of them to run? Make an `all` target. Since this is the first rule listed, it will run by default if `make` is called without specifying a target.

```
all: one two three

one:
	touch one
two:
	touch two
three:
	touch three

clean:
	rm -f one two three
```

There are many [automatic variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html), but often only a few show up:

```
hey: one two
	# Outputs "hey", since this is the target name
	echo $@

	# Outputs all prerequisites newer than the target
	echo $?

	# Outputs all prerequisites
	echo $^

	touch hey

one:
	touch one

two:
	touch two

clean:
	rm -f hey one two
```