---
tags: vim
---
inoremap: maps the key in insert mode
nnoremap: maps the key in normal mode
vnoremap: maps the key in visual mode
<C>: Represents the control key
<A>: Represents the alt key.

================================================
Search from the current line :,$s/old/new/c
Search in case insensitive way: /keyword\c

exact search: /\<some word\>
exact search and replace: %s,\<word to replace\>,someword,gc

find project -name '*.rb' -type f -exec sed -i -e 's/regex/replacement/g' -- {} +

To ignore case type :set ignorecase or :set ic in the Vim command line.
================================================

remove swap files: rm ./.*swp
open a tab page:tabedit <filename>
In normal mode: gt or gT to move next or previous tab pages

Switch tab position: tabmove {#1,2,3,4...}

================================================
ctags: go to the project folder and type `ctags -R .` >> Create tags
ctags search: `^+]`

ct) : cut until )
================================================
code folding:
1) in visual mode select code lines...
2) :fo
3) unfold: z,o //// za
Unfold all
:zR

Visual folding: zf
================================================
Cursor moving
C : change whole line
ciw: change inside word
ct]: change till ]

f/F {char}: next occurence of char
; :repeat last f command

<C-e>: scroll down without moving a cursor
<C-y>: scroll up without moving a cursor
================================================
Indentation 
- Reformat all indentations in a script:
:%s/^\s*/&&/g

= : Visual block indent
gg=G : indent all

================================================
Switch pane positions
(C w) r
================================================
u: make lowercase
U: make uppercase
fin {file}: open file

================================================
Marking: 
'.: jumping to the last change
m{a-zA-Z}: sets a custom mark whose exact location can be accessed using '{mark}

===============================================
Paste in Command mode
<C-R> "

Get currrent file path
<C-R> %
===============vimlatex=========================
\ll
<F5>
<C-j>

:PDF %:r

function! s:PDFLATEX(...)
	execute printf('!pdflatex -synctex=1 -interaction=nonstopmode %s.tex', a:1)
	execute printf('!bibtex %s.aux', a:1)
endfunction
command! -nargs=1 PDF call s:PDFLATEX(<f-args>)

================================================
open terminal below
:bel ter    

set terminal size:
:bel ter ++rows=5

close term:
<C-c> or <C-d>

================================================
Ctrl+Q to unfreeze Ctrl+S issue

================================================
Command History:
q:

================================================
Wrap a long paragraph:
in command mode: gqq

================================================
AutoComplete
^x^f: autocomplete path
^n: autocomplete


================================================
WrapUp Long Text
gww

================================================
Turn off markdown error:
But that would cause the other syntax rules to start an italic section on that _ char. Better just clear the error highlighting with:

:hi link markdownError Normal

To maintain the general error highlighting, but only define exceptions for the special $x_i$ string, define an overriding syntax group; luckily, this is easy because no existing syntax is there:

:syn match markdownIgnore "\$x_i\$"

===============================
Command line window
:<C-f>
:help command-line-window
<C-r>" : yank to command line (ctrl+r+")


==============================================
NERDTree
t: open the selected file in a new tab
i: open the selected file in a horizontal split window
s: open the selected file in a vertical split window
m: show the nerd tree menu
(Shift-a): expland nerd tree and fold 
Press I ( Shift + i ) to toggle hidden files in the NERDTree explorer window**.








