
## Testing Conditions

There are many test operations:
- File tests 
- String tests 
- Arithmetic tests 

### File tests
Most file tests, like `-f`, are called _unary_ operations because they require only one argument: the file to test.
- `[ -f file]` : Check whether `file` is a regular file, not a directory or special file.
```sh
for filename in *; do
	if [ -f $filename]; then
		ls -l $filename
		file $filename
	else
		echo $filename is not a regular file.
	fi
done
```
- `-e` : returns true if a file exists
	- `-f`: Checks if file exists and is a file.
	- `-d`: Checks if a directory exists.
- `-s` : returns true if a file is not empty
Permissions:
	- `-x`: Checks if file exists and is executable.
	- `-r`: Checks if file exists and is readable.
	- `-w`: Checks if file exists and is writable.
- `[ file1 -nt file2]` : this binary operation tests whether `file1` has a newer modification date than `file2`.

### String Tests
- `str1=str2`: Checks if str1 is the same as string str2
- `!=`
- `-z` : returns true if its argumet is empty. `[ -z ""]` returns 0
- `-n` : returns true if its argument is not empty. `[ -n ""]` returns 1

### Arithmetic Tests 
- Note that the equal sign (`=`)  looks for string equality, not numeric equality. 
	- `[ 1 = 1 ]` returns 0, but `[ 01 = 1 ]` returns false.
- `-eq` : equal to, `[ 01 -eq 1 ]` returns true
- `-ne` : not equal to
- `-lt` : less than
- `-gt` : greater than
- `-le` : less than or equal to
- `-ge` : greater than or equal to