---
tags: regular_expression
---
https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285

# Introduction

Many different applications use different types of regex in Linux, like the regex included in programming languages (Java, Perl, Python,) and Linux programs like (sed, awk, [grep](https://likegeeks.com/grep-command-in-linux/),) and many other applications.

A regex pattern uses a regular expression engine that translates those patterns.

Linux has two regular expression engines:
- The **Basic Regular Expression (BRE)** engine (`sed, python`).
- The **Extended Regular Expression (ERE)** engine (`awk`).

Most Linux programs work well with BRE engine specifications, but some tools like `sed` understand some of the BRE engine rules.

The POSIX ERE engine comes with some programming languages. It provides more patterns, like matching digits and words. The `awk` command uses the ERE engine to process its regular expression patterns.

You can define a pattern to match text like this:
- `echo "Testing regex using sed" | sed -n '/regex/p'`
- `echo "Testing regex using awk" | awk '/regex/{print $0}'`


# Syntax

We use the dot character to match any character except the newline (`\n`).
### Anchors
`^The`        matches any string that **starts with** **The**
`end\$`        matches a string that **ends with** end 
`^The end\$`   exact string match** (starts and ends with **The end**)
`roar`        matches any string that **has the text roar in it**

### Quantifiers

### Bracket Expressions (or Character Classes)
`[abc]`: matches a string that has **either an a or a b or a c** -> is the **same as a|b|c**
	- `awk '/[oi]th/{print $0}' myfile`
	- Here we search for any th characters that have `o` character or `i` before it.
`[a-c]`: same as previous, but it uses _range_
`[a-fA-F0-9]`: a string that represents **a single hexadecimal digit, case insensitively**
`[0-9]%`:  a string that has a character **from 0 to 9 before a % sign**
`[^a-zA-Z]` :  a string that has **not a letter from a to z or from A to Z.** In this case the **^** is used as **negation of the expression** 

`\w`: any alphanumeric
`\W`: any non-alphanumeric
`\d` : any digits
`\D` : any non digits
`\s`: any white space (spcae, tab, newline)
`\S`: any non white space
`{m}`: m-repetition. For instance, `a{3}` will match the `a` character exactly three times. `[wxy]{5}`.
`{m,n}`: m-n repetition

### Group
Regular expressions allow us to not just match text but also to _extract information for further processing_. 
- This is done by defining _groups of characters_ and capturing them using the special parentheses _(_ and _)_ metacharacters. 
- Any subpattern inside a pair of parentheses will be _captured_ as a group. In practice, this can be used to extract information like phone numbers or emails from all sorts of data.

You can group expressions so the regex engines will consider them one piece.
- `echo "Like" | awk '/Like(Geeks)?/{print $0}'`

Imagine for example that you had a command line tool to list all the image files you have in the cloud. 
- You could then use a pattern such as `^(IMG\d+\.png)$` to capture and extract the full filename, but _if you only wanted to capture the filename without the extension_, you could use the pattern `^(IMG\d+)\.png$` which only captures the part before the period.

[Ref](https://regexone.com/lesson/capturing_groups)
