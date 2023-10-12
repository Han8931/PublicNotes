---
tags: regular_expression, linux, grep
---

Ref: LukeSmith

## sed

## grep

The grep tool has the following options to use regular expressions:
- -E : String is read as ERE (Extended Regular Expressions)
- -G : String is read as BRE (Basic Regular Expressions)
- -P : String is read as PRCE (Perl Regular Expressions)
- -F : String is read literally.

Syntax:
- `grep <pattern> <fileName>`

### Basics
- `grep "word/charcter" <filename>` : grep stands for global regular expression print
- `.` : period is for any character
	- confixation/ fix/ fox/ fax: `grep "f.x" <filename>`
- `*` : repeat the any number of the previous charcter  (0-)
	- fiiiiiiix / foooox / fx :  `grep "f.*x" <filename>`
- `+` : repeat the any number of the previous charcter  from 1
	- fiiiilx/ foooox :  `grep "f.\+x" <filename>`
	- `\` is necessary for running in shell. 
- `$` : match with the end of the line
	- fox/ fax/ xerox: `grep "x$" <filename>`
- `^` : match with the beginning of the line
	- xpool/ xeros : `grep "^x" <filename>`
- `\S` : Any non-whitespace character
	- boomer / zoomer/ doomer/ a coomer/ the consoomer: `grep "\S*oomer <filename>"
- `\s` : Any whitespace character
	- the           consoomer: `grep "the\s\+conoomer <filename>"
- `?` : Optional
- `\` : escape something
- `[a-z]` : any lowercase letter
- `[A-Z]` : any uppercase letter
- `[a-zA-Z]` : any letter
- `[0-9]` : any digits/number
	- `[5-9]`

The pipe (|) symbol is used as OR to signify one or the other. All the three versions are shown. Options -E and -P syntax are same but -G syntax uses (\).

**Syntax:**
- `grep <option> <'pattern|pattern> <fileName>`
	- `grep -E 'j|g' msg.txt  `
	- `grep -P 'j|g' msg.txt`
 
Regex patterns use some special characters. And you can’t include them in your patterns, and if you do so, you won’t get the expected result.

These special characters are recognized by regex:
`.*[]^${}\+?|()`

You need to escape these special characters using the backslash character (`\`). For example, if you want to match a dollar sign (`$`), escape it with a backslash character like this:
`awk '/\$/{print $0}' myfile`

If you need to match the backslash (\) itself, you need to escape it like this:
`$ echo "\ is a special character" | awk '/\\/{print $0}'`

## Extended regular expressions

- The question mark means the previous character can exist once or none.
- The plus sign means that the character before the plus sign should exist one or more times, but must exist once at least.
- The pipe symbol makes a logical OR between 2 patterns. If one of the patterns exists, it succeeds; otherwise, it fails, here is an example:
	- `echo "This is something else" | awk '/regex|regular expressions/{print $0}'`
- You can group expressions so the regex engines will consider them one piece.

### Curly braces
Curly braces enable you to specify the number of existence for a pattern, it has two formats:
- `{n}`: The regex appears exactly `n` times.
- `{n,m}`: The regex appears at least `n` times, but no more than `m` times.


#### URL Matching
- http / https : `grep "http\?" <filename>`
- http:// / https://abcd.com : `grep "http\?://\S*\.[a-zA-Z]\+" <filename>`

#### Email Matching
- `grep "\S\+@\S\+\.[a-zA-Z]\+" <filename>`

#### Email Validating
`echo "name@host.com" | awk '/^([a-zA-Z0-9_\-\.\+]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/{print $0}'`


