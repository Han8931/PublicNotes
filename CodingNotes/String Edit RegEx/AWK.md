General pattern: `awk 'pattern {action}' ~/scripts`

- `ps | awk '{print $1}'`: print the first column
	- `ps | awk '{print $1 $2}'`: print the first and the second columns
	- `ps | awk '{print $1" "$2" "}'`: print the first and the second columns with an empty space
	- `ps | awk '{print $1"\t"$2"\t"}'`: print the first and the second columns with a tab
- `ps | awk '{print $0}'`: print all
- ` awk -F ":" '{print $1}' cat /etc/passwd` : Set a colon as deliminator. 
- `awk 'BEGIN{FS=":"; OFS="-"} {print $1,$6,$7}' /etc/passwd`
	- Perform the actions with the separator `:` and output it with dash.
- `awk -F "/" '/^\// {print $NF}' /etc/shells | uniq | sort`:
	- Set `/` as a separator
	- `^\/`: Find a pattern that starts with `/`.
		- Note that the backslash `\` is the escape. When using awk, you have to escape it. 
		- The search pattern has to be wrapped between `/ /`
	- Finally, print the last one `NF`
	- And take only unique items and sort them
- `df | awk '\/dev\/loop\/ {print $1}'`
	- `df | awk '\/dev\/loop\/ {print $1"\t"$2+$3}'`: Add the memory
- `awk 'length($0) > 7' /etc/shells`: print only lines that are longer than 7.
- `ps -ef | awk '{ if($NF == "/bin/bash") print $0}'`
- `awk 'BEGIN {for(i=1; i<=10;i++) print "The square root of", i*i, "is", i;}'`
- `awk '$1 ~ /^[b,c]/ {print $0}' .bashrc`
	- AWK expressions include the tilde operator, `~`, which matches a regular expression against a string.
	- `~` checks to see if its left operand matches its right operand; `!~` is its inverse. Note that a regular expression is just a string and can be stored in variables.

## Pre-defined and Automatic Variables in AWK
- `RS`: The record separator.
- `NR`: The current input record number. If you are using the standard newline delimiter for your records, this match with the current input line number.
- `FS/OFS`: The character(s) used as the field separator
- `NF`: The number of fields in the current record. If you are using the standard "white space" delimiter for your fields, this will match with the number of words in the current record.

## A Basic Usage of AWK Command

Example `file`:
```text
CREDITS,EXPDATE,USER,GROUPS
99,01 jun 2018,sylvain,team:::admin
52,01    dec   2018,sonia,team
52,01    dec   2018,sonia,team
25,01    jan   2019,sonia,team
10,01 jan 2019,sylvain,team:::admin
8,12    jun   2018,öle,team:support
        


17,05 apr 2019,abhishek,guest
```
### Print All Lines
Basic pattern: `awk pattern {action}`
- `awk '1 { print }' file`
	- If, for a given __record__ (“line”) of the input file, the __pattern__ evaluates to a non-zero value (equivalent to “true” in AWK), the commands in the corresponding __action block__ are executed. In the above example, since `1` is a non-zero constant, the `{ print }` action block is executed for each input record. 
### Remove a File Header
```
awk 'NR>1 { print }' file
```
Since this program is using the default values for `RS`, in practice it will discard the first line of the input file.

### Print Lines in a Range
```
awk 'NR>1 && NR < 4 {print}' file
```

### Removing Whitespace-Only Lines
```
awk 'NF' file
```

AWK splits each record into fields, based on the field separator specified in the `FS` variable. The default field separator is __one-or-several-white-space-characters__ (aka, spaces or tabs). With those settings, any record containing at least one non-whitespace character will contain at least one field.

In other words, the only case where `NF` is 0 (“false”) is when the record contains only spaces. So, that one-liner will only print records containing at least one non-space character.

### Removing All Blank Lines
```
awk '1' RS='' file
```

