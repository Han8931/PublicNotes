The `sed` stands for Stream EDitor. This command allows you to parse and transform text data. If the input originates from a file, a pipeline, or standard input, `sed` processes it line by line.

With `sed`, you can perform various text manipulations like insertion, deletion, search, and replacement.

## Basic Syntax and Operation

The basic structure for the `sed` command is:
`sed 'COMMAND' file_name`
- Where `COMMAND` is the operation you wish to perform, and `file_name` is the name of the file you’re working with.
- If you omit the file name, `sed` will expect input from standard input as follows:
	- `echo "Linux is fun" | sed 's/fun/great/'`
	- Output: `Linux is great`

This pipes the output of `echo` into `sed`, which then replaces "fun" with "great".

### Specifying files as input

If you want `sed` to process a file directly, specify the file name.
- `sed 's/Linux/UNIX/' sample.txt`
Assuming `sample.txt` contains the line "Linux is Awesome", the output would be:
- `UNIX is Awesome`

To edit the file in-place and save the changes, use the `-i` option.
- `sed -i 's/Linux/UNIX/' sample.txt`
After this command, the content of `sample.txt` will permanently change to "UNIX is Awesome".

### Specifying Line numbers

You can specify a particular line number to restrict a command’s effect.
- `echo -e "Apple Banana\nBanana\nCherry" | sed '2s/Banana/Peach/'`

Output:
```
Apple
Peach
Cherry
```
Only the second line, "Banana", gets replaced with "Peach".

### Address Ranges

You can specify a range of lines by indicating the start and end line numbers.
`echo -e "Apple\nBanana\nCherry\nDate\nElderberry" | sed '2,4s/^/Fruit: /'`
- Restrict the range to 2-4
- Replace (`s`) the first place (`^`) with `Fruit: `

Output:
```
Apple
Fruit: Banana
Fruit: Cherry
Fruit: Date
Elderberry
```
Lines 2 through 4 have been prefixed with "Fruit: ".

## Substituting text

The `s` command searches for a specified pattern and replaces it with another.
The basic syntax for substitution in `sed` is:
- `sed 's/pattern/replacement/'`

Command:
- `echo "Cats are cute." | sed 's/cute/beautiful/'`
Output:
- `Cats are beautiful.`
Here, the word "cute" is replaced with "beautiful".

### Global Substitution

By default, `sed` replaces only the first occurrence in each line. To replace all occurrences, append the `g` flag.
`echo "Cats are cute. Dogs are cute too." | sed 's/cute/beautiful/g'`

Output:
`Cats are beautiful. Dogs are beautiful too.`
Both instances of "cute" are replaced with "beautiful".

### Change Slash Delimiter

While most examples use the forward slash `/` as the delimiter, you can pick other characters, especially when dealing with file paths or URLs.
`echo "Visit http://example.com" | sed 's_http://_https://_'`

Output:
`Visit https://example.com`
This switches an HTTP URL to HTTPS, and uses underscores as delimiters to avoid clashing with slashes in the URL.

## Delete lines

The `d` command in `sed` allows you to delete lines based on specific criteria, be it a direct match, a regular expression, or an address range.

### Delete a Specific Line

To delete a specific line, provide its line number.
`echo -e "Apple\nBanana\nCherry" | sed '2d'`

Output:
```
Apple
Cherry
```
The second line, "Banana", is removed from the output.

### Delete a Range of Lines

You can specify a range of lines to be deleted.
`echo -e "Apple\nBanana\nCherry\nDate\nElderberry" | sed '2,4d'`

Output:
```
Apple
Elderberry
```
Lines 2 through 4 (inclusive) are deleted.

### Delete Lines Matching a Pattern

You can delete lines matching a specific pattern using regular expressions.
`echo -e "Apple\nBig Banana\nCherry\nBig Date\nElderberry" | sed '/^Big /d'`

Output:
```
Apple
Cherry
Elderberry
```

All lines beginning with "`Big `" are removed from the output.

### Delete All Except Lines Matching a Pattern

Sometimes, instead of deleting lines that match a pattern, you’ll want to keep only those lines and delete everything else. This can be achieved using the inverse match `!`.
`echo -e "Apple\nBig Banana\nCherry\nBig Date\nElderberry" | sed '/^Big /!d'`

Output:
```
Big Banana
Big Date
```
Only lines starting with "`Big `" are retained in the output.


## Printing lines

The `p` command in `sed` prints lines from the input, and when combined with various patterns or address ranges, it becomes a powerful tool for displaying specific content.

### Printing a Specific Line

To print a certain line, just indicate its line number.
`echo -e "Apple\nBanana\nCherry" | sed -n '2p'`

Output:
```
Banana
```

Only the second line, "Banana", is displayed.

### Printing a Range of Lines

Defining a range of lines allows you to selectively print multiple lines.
`echo -e "Apple\nBanana\nCherry\nDate\nElderberry" | sed -n '2,4p'`

Output:
```
Banana
Cherry
Date
```
Lines 2 through 4 are printed.

### Printing Lines Matching a Pattern

With a regular expression, you can instruct `sed` to print lines that match a certain pattern.
`echo -e "Apple\nBig Banana\nCherry\nBig Date\nElderberry" | sed -n '/^Big /p'`

Output:
```
Big Banana
Big Date
```
Only lines beginning with "`Big `" are printed.

### Double Printing Lines Matching a Pattern

If you use the `p` command without the `-n` option, `sed` will print each line of the input by default. When a line matches a pattern or address, it gets printed again.
`echo -e "Apple\nBig Banana\nCherry\nBig Date\nElderberry" | sed '/^Big /p'`

Output:
```
Apple
Big Banana
Big Banana
Cherry
Big Date
Big Date
Elderberry
```
Lines starting with "`Big `" are printed twice.


## Grouping & Back-references

Grouping and back-references are powerful features in `sed` that allow you to capture portions of text and reference them in your operations.

Use the escape-prefixed parentheses `\(` and `\)` to group parts of your pattern.
`echo "The apple is red" | sed 's/\(apple\)/fruit: \1/'`

Output:
`The fruit: apple is red`
The term "apple" is captured and referred to as `\1` in the replacement string.

### Using Multiple Back-references

You can have multiple groups and reference them using `\1`, `\2`, etc.
`echo "Swap this around" | sed 's/\(Swap\) \(this\) \(around\)/\3 \2 \1/'`

Output:
`around this Swap`

The words "Swap", "this", and "around" are captured and rearranged in the replacement.

**Example: Renaming Files using Back-references**

Back-references can be particularly useful in scripts for tasks like renaming files.

Consider a situation where you have filenames in the format "file-001.txt" and you wish to rename them to "001-file.txt".

Command (hypothetical usage in a script):
`echo "file-001.txt" | sed 's/\(file\)-\(.*\).txt/\2-\1.txt/'`

Output:
`001-file.txt`

### Regex inside Parentheses

You can use regular expressions inside grouping parentheses to capture dynamic content and utilize it in transformations.
`echo "Price: $5.99" | sed 's/Price: $\(.*\)/The cost is \1/'`

Output:
`The cost is 5.99`

## Changing Case with y Command

The `y` command in `sed` enables you to transform characters from one set to another, which is particularly useful for changing the case of text.

Unlike the `s` command, `y` operates on individual characters rather than patterns.

### Changing to Uppercase

To convert a string to uppercase, specify the range of characters to be transformed.
`echo "make this uppercase" | sed 'y/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/'`

Output:
`MAKE THIS UPPERCASE`

Every lowercase letter is transformed to its uppercase counterpart.

### Changing to Lowercase

Similarly, you can change text to lowercase.
`echo "MAKE THIS LOWERCASE" | sed 'y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/'`

Output:
`make this lowercase`

Each uppercase letter is swapped for its lowercase equivalent.

### Mixing Case Transformations

In some situations, you may want to swap the case of each letter.
`echo "Mix\ntHiS\nCaSe" | sed 'y/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/'`

Output:
`mIX ThiS cAsE`

Every lowercase character is turned to uppercase, and vice versa.

### Limiting the Transformation Scope

By combining the `y` command with addresses or patterns, you can restrict the scope of the transformation.
`echo -e "Change\nTHIS\nLine" | sed '/THIS/y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/'`

Output:
```
Change
this
Line
```
Only the line containing “THIS” is converted to lowercase.


