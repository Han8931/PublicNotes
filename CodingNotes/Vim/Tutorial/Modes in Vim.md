### Normal Mode
- `daw`: delete a word backword
- `db`: delete a word backword except the current character

- Addition and subtraction:
	- `<C-a>`: perform addition on numbers
	- `<C-x>`: perform subtraction on numbers
	- The above commands work on at the beginning of the sentence too
		- Try this `.blog { background-position: 0px 0px }`
- Indentation: `=`
	- Autoindent all lines: `gg=G`
- `<C-r>{register}`, where {register} is the address of the register we want to insert. 
- `<C-a>`: increase the number 
- `<C-x>`: decrease the number

### Visual Mode
- `<C-v>`: enable block-wise visual mode
- `gv`: reselect the last visual selection
- `o`: go to other end of highlighted text
- `vit`: visually select the inner contents of a tag:
	- `<a href="#">one</a>` : if we use `vit`, then it would show `one`
	- Since, `one` is the inner content surrounded by tags
- When we hit `c` after visullay selecting some texts, all of the selected text disappear and change to insert mode

#### Append After a Ragged Visual Block
```
var foo = 1
var bar = 'a'
var foobar = foo + bar
```
1. `<C-v>jj$`
2. `A;`
3. `<ESC>`
```
var foo = 1;
var bar = 'a';
var foobar = foo + bar;
```

*A better approach is*: 
1. `A;` at the first line
2. Visually block target lines
3. `:'<,'>normal .`: `.` is the repeat command in the `normal` mode. 
	- **For a complex command to apply on multiple lines, use _macro_!!**
	- `:'<,'>normal @a`: 

### Command Line Mode
```html
<!DOCTYPE html>
<html>
	<head><title>Practical Vim</title></head>
	<body><h1>Practical Vim</h1></body>
</html>
```
- `:p`: print the current line
	- `:{range}p`: for instance, ``:2,5p``
	- We can use the `.` symbol as an address to _represent the current line_. So, we can easily compose a range representing everything from here to the end of the file:
		- `.,$p`
	- `%`:  represents the entire file range. 
	- `$`: last line of the file
- If we select lines visually, and then press `:`, the command line prompt will show the following range
	- `:'<,'>p`: `'<.'>` is the range of selected visual block. Thus, this command prints the visually selected block. 
	- The `'<` symbol is a mark standing for the first line of the visual selection, while `'>` stands for the last line of the visual selection
- Vim also accepts a pattern as an address for an Ex command, such as the one shown here:
	- `:/<html>/,/<\/html>/p`
	- This looks quite complex, but it follows the usual form for a range: `:{start},{end}`. The `{start}` address in this case is the pattern `/<html>/`, while the `{end}` address is `/<\/html>/`. In other words, the range begins on the line containing an opening `<html>` tag and ends on the line containing the corresponding closing tag.
	- Suppose that we wanted to run an Ex command on every line inside the `<html></html>` block but not on the lines that contain the `<html>` and `</html>` tags themselves. We could do so using an offset:
		- `:/<html>/+1,/<\/html>/-1p`
	- `:.,.+3p`: this is equivalent to `:2,5p` if the current line is at 2.
- We can execute any normal mode commands as follows:
	- `%normal A;`: append `;` at the end of all lines in the file (due to the `%`). 
- We can run shell commands by
	- `:!ls`
	- `:!python %`: `%` is shorthand for the current file name

#### Sort Texts
```
first name,last name,email
john,smith,john@example.com
drew,neil,drew@vimcasts.org
jane,doe,jane@example.comk
```

We’ll sort the records by the second field: last name. We can use the `-t','` option to tell the sort command that fields are separated with commas, and we can use the `-k2` flag to indicate that the second field is to be used for the sort.
- `-t`: seperated by
- `-k`: field

The first line of the file contains header information. We want to leave it at the top of the file, so we’ll exclude it from the sort operation by using a range of `:2,$`. This command line does what we want:
- `:2,$!sort -t',' -k2`
 
#### Replace Mode 
- `R`: engage replace mode.
