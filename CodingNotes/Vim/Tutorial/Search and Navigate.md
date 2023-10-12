Reference: Practical Vim

## Search & Navigate
- `>G`: increase the indentation from the current line until the end of the line.
- `f`: look ahead (forward)
- `;`: repeat the last search
	- For instance, if you are looking for the next occurence of `+`, then `f+`, and to repeat this `;`.
- `.` : period command repeats the last change. 
- `*`: the cursor will jump forward to the next match
- Delete currrent sentence:
	- `dis` or `das`
 
### Text Object
Text objects allow us to interact with parentheses, quotes, XML tags, and other common patterns that appear in text. 

Vim understands the structure of these well-formed patterns, and it allows us to _operate on the regions of text that they delimit_. Text objects define regions of text by structure. 

```
var til = [
'<a hief="{url}">{title}</a>'
]
```
Let's try to visually select the text, then change to visual mode and 
- `i}`: Inside of braces
- `a"`: A pair of double quotes
- `i>`: Inside of angle brackets
- `i]`: Inside of brackets
- `a]`: A pair of brackets

### Automatic Marks
- \`\`:  Position before the last jump within current file
- \`. :  Location of last change
- \`^ : Location of last insertion
- \`<: Start of last visual selection

### Jump Between Matching Parentheses
The `%` command lets us jump between opening and closing sets of parentheses. 
```
console.log([{'a':1},{'b':2}])
```
Note that `%` command only works on well-formed matching parentheses. 

### Traverse the Jump List
The following commands allow use to traverse Vim's jump list. _Jumps can move between files_. We can inspect the contents of the jump list by running this command:
- `:jumps`

Then, we can traver by using the following commands:
- `<C-o>`: Jump backward
- `<C-i>`: Jump forward

### Traverse the Change List
`:changes`: show a list of changes
`:g;`:traverse backward
`:g,`:traverse forward

### Traverse to the Filename Under the Cursor
Vim treats filenames in our document as a kind of hyperlink. When configured properly, we can use the `gf` command to go to the filename under the cursor.

Then, we can go back to where we came from using the `<C-o>`

#### Specify the Directories to Look Inside

In this example, each of the files referenced with the require statement was located relative to the working directory. But what if we referenced functionality that was provided by a third-party library, such as a rubygem? 

That’s where the 'path' option comes in. We can configure this to reference a comma-separated list of directories. When we use the gf command, Vim checks each of the directories listed in 'path' to see if it contains a filename that matches the text under the cursor. The ‘path’ setting is also used by the `:find` command.

We can inspect the value of the path by running this command: 
```
:set path?
>>path=.,/usr/include,, 
```

In this context, the `.` stands for the directory of the current file, whereas the empty string (delimited by two adjacent commas) stands for the working directory. The default settings work fine for this simple example, but for a larger project we would want to configure the ‘path’ setting to include a few more directories.

Use commas to separate directory names (c.f., `:h path`):
`:set path=.,/usr/local/include,/usr/include`

### Snap between Files Using Global Marks
- `m{letter}`: allows us create a mark at the current cursor position. 
	- Lowercase letters create marks that are local to a buffer.
	- Uppercase letters create global marks.
- `` `{letter}``: Snap our cursor back to it.

#### Tip
open up your vimrc file and press `mV` to set a global mark (mnemonic: V for vimrc). Switch to another file and then press `` `V ``, and you should snap back to the global mark you set in the vimrc file.
	
## Macro
- `q{register}`
- `@{register}`
- `@@`: repeat the last macro
- `10@a`: repeat the macro ten times.


Find and replace all words recursively in a dire
```bash
find . -type f -name "*.txt" -print0 | xargs -0 sed -i '' -e 's/foo/bar/g'
```

```bash
#!/bin/bash
# find_and_replace.sh

echo "Find and replace in current directory!"
echo "File pattern to look for? (eg '*.txt')"
read filepattern
echo "Existing string?"
read existing
echo "Replacement string?"
read replacement
echo "Replacing all occurences of $existing with $replacement in files matching $filepattern"

find . -type f -name $filepattern -print0 | xargs -0 sed -i '' -e "s/$existing/$replacement/g"
```

