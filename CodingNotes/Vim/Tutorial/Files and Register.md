## Files
Just like any other text editor, Vim allows us to read files, edit them, and save our changes. When we discuss our workflow, it’s tempting to say that we’re editing a file, but that’s not what we’re actually doing. Instead, we’re _editing an in-memory representation of a file_, which is called a _buffer_ in Vim’s terminology

_Files are stored on the disk, whereas buffers exist in memory_. When we open a file in Vim, its contents are read into a buffer, which takes the same name as the file. Initially the contents of the buffer will be identical to those of the file, but the two will diverge as we make changes to the buffer. If we decide that we want to keep our changes, we can write the contents of the buffer back into the file. Most Vim commands operate on buffers, but a few operate on files, including the `:write`, `:update`, and `:saveas` commands.

## Register 
Rather than using a single clipboard for all cut, copy, and paste operations, Vim provides multiple registers. When we use the delete, yank, and put com mands, we can specify which register we want to interact with.

### Addressing a Register
We can specify which register we want to use by prefixing the command with `"{register}`. If we don’t specify a register, then Vim will use the unnamed register.

For example, if we wanted to yank the current word into register `a`, we could run `"ayiw`. Or if we wanted to cut the current line into register b, we could run `"bdd`. Then, we could paste the word from register `a` by typing `"ap`, or we could paste the line from register `b` by typing `"bp`.

>Vim’s yank command is equivalent to the copy operation. Historically, the `c` command was already assigned to the change operation, so vi’s authors were pushed to come up with an alternative name. The `y` key was available, so the copy operation became the yank command.


### Unnamed Register ("")
If we don't specify which register we want to interact with, then Vim will use the unnamed register, which is addressed by the `"` symbol.

### Yank Register ("0)
When we use the y{motion} command, the specified text is copied not only into the unnamed register but also into the yank register, which is addressed by the `0` symbol. 

We can inspect the contents of the unnamed and yank registers by
`:reg "0`

### Black Hole Register
The black hole register is a place from which nothing returns. It’s addressed
by the underscore symbol (see `:h quote_` ). If we run the command `"_d{motion}`, then Vim deletes the specified text without saving a copy of it. This can be useful if we want to _delete text without overwriting the contents of the unnamed register_.

### The System Clipboard ("+) and Selection ("\*) Registers.
All of the registers that we’ve discussed so far are internal to Vim. If we want to copy some text from inside of Vim and paste it into an external program (or vice versa), then we have to use one of the _system clipboards_.

Vim’s plus register references the system clipboard and is addressed by the `+` symbol.

If we use the cut or copy command to capture text in an external application, then we can paste it inside Vim using `"+p` command (or `<C-r>+` from the Insert mode). Conversely, if we prefix Vim’s yank or delete commands with `"+`, the specified text will be captured in the system clipboard. That means we can easily paste it inside other applications.

- `"+`: The X11 clipboard, used with cut, copy. and paste.
- `"*`: The X11 primary, used with middle mouse button.
	-  The X11 windowing system has a second kind of clipboard called the _primary_. This represents the most recently selected text, and we can use the middle mouse button (if we have one) to paste from it. Vim’s quotestar register maps to the primary clipboard and is addressed by the `*` symbol.

### Expression register
- Expression register can be used to evalute commands and return the result in the insert mode.
	- e.g., simple calculation
- `<C-r>=` : The expression register is addressed by the `=` symbol. 

### More Registers
- `"%`: Name of the current file
- `"#`: Name of the alternate file
- `".`: Last inserted text
- `":`: Last Ex command
- `"/`: Last search pattern. 

## Buffer
- `ls`: list buffers
- `bd <name>` or `bdelete <name>` : delete buffers
- `buffer <name>`: switch to a buffer
	- or `buffer N`  , `N` is the buffer index
	- For example `buffer3`
- Switch between buffers
	- `bprevious` or `bnext`
	- Simply type `bp` or `bn`

Some more information about a buffer is also shown by the following flags:
- `%` : Buffer which is in the current window
	- The file name of the current window without its file extension is `%:r`
- `#` : Alternate buffer (the last file which was most recently edited in the current window)
- `a` : Active buffer (the file which is being edited in the current window)
- `h` : Hidden buffer (buffer with unsaved modifications but is not being displayed in any window)
- `u` : Unlisted buffer (files that are not open in Vim but are present in the current working directory; use `:ls!` to view this)
- `-` : Buffer with 'modifiable' set to off
- `=` : A read-only buffer
- `+` : A modified buffer (buffer with changes that are not written to disk)
- `x` : A buffer that has read errors