# Basics 

The sed ( sed is a short for "stream editor") program is an automatix text editor that takes an input stream, alters it according to some expression, and prints the results to standard output. Sed is a stream editor by default, which does not modify a file.

```toppings.txt
Pizza topping combos:
1. Spinach, Pepperoni, Pineapple
2. Pepperoni, Pineapple, Mushrooms
3. Bacon, Banana Peppers, Pineapple
4. Cheese, Pineapple
```


## Substitution
- `sed 's/find/replace/g' < oldfile > newfile`
	- Simply, `sed -i 's/find/replace/' newfile`: 
		- `-i`: inplace 
	- Find and replace from oldfile and output to newfile
- `echo "The Vim file is ainticipated" | sed 's/ant/bug/g'`:
	- Output is: `The Vim file is bugticipated`. 
	- However, this is not what we want. 
- Actually, you can use any delimiter instead of the forward slash `/`. What if you wanna find a pattern with the forward slash? For instance a path like `/etc/`. You can simply use another delimiter: 
	- `sed 's /etc /somedir'` or `sed 's./etc./somedir'`
- To recursively find and change:
	- `find . -type f -name '*.py' | xargs sed -i 's/Real/float/g'`

## Print Lines
- `sed -n '1p' file.txt`: print only first line
	- `sed -n '1,3p' file.txt`: print 1-3 lines
	- `sed -n '3,$p' file.txt`: print 3-end lines
	- `sed -n '1,$p' file.txt`: print all lines
	- `sed -n -e '1p' -e '8,$p' file.txt`: print first line and line 8 to end

## Delete Lines
- `sed -n '1d' file.txt`: delete first line

# Sed with RegEx

- `sed` : is a stream editor by default. We are not modifying a file
	- If we want to change the file, then run with `-i` argument. 
- `sed "s/c/C/g" <file>` : 
	- `s` : substitute `c` to `C`
	- `g` : without `g` it will change once for a line at the first appearance of `c`
	- To delete all `c` : `sed "s/c//g" <file>`
	- `p` : print
	- `q` : quite the file
 
### Examples
- To remove all comments : `sed "s/#.*//g" <file>`
- To remove all comments and whitespace if front of `#`: `sed "s/\s*#.*//g" <file>`
- We can also concatenate different sed commands with a semicolon:
	- `sed "s/\s*#.*//g;s/c/C/g" <file>`
- To remove all lines start with `cf`:  `sed " /cf/ d" <file>`
	- Find texts starting with `cf` and delete them with `d` argument
- To remove blank lines:
	- `sed " /^$/ d" <file>` : blank line is the one with the beginning line with (`^`) the end of the line(`$`).





