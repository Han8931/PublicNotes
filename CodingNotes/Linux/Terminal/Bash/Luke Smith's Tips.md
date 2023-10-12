---
tags: linux, bash, terminal, script
---

- `echo $SHELL` to check my shell type
- `#!/bin/bash ` : determine which shell type to use
	- `chmod u+x shelltest.sh` : then we can run it by simply `./shelltest.sh`
- Assign a variable and refer it by $ symbol.
- `read` : get variables
- Positional arguments: `$1 $2`
- `[ hello = hello ]` : compare
	- `echo $?`
 
- `;` execute multiple commands
	- `echo "Hello there"; echo "General \!"`
- `&&` (and) : It only runs the second command if the first one was successful.
	- If the first command's exit code is 0, the shell also runs command 2
- `||` (or) : It only runs the second command if the first one was not successful.
	- Run the second one only when the first exit code is non-zero
- `&` :  The above three commands wait for the first command, but a single `&` just run the second one immediately.

- *This is an ugly approach*
```bash
#!/bin/bash

if [ "$EDITOR" = "" ]; then
	EDITOR=nano
fi
echo $EDITOR
```
- *Elegant method*
```sh
#!/bin/bash

[ -z "$EDITOR" ] && EDITOR=nano
echo $EDITOR
```