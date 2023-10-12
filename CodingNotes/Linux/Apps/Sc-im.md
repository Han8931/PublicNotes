---
tags: vim, sc-im, spreadsheet
---
`>` : type text right aligned
`<` : type text lef aligned
`\` : type text middle aligned
`=` : type number

`aa` : show long text (asterisks..)
`f-`: decrease precision
`f+`: increase precision
`e`: edit number
`E`: edit text
`f>`: increase column width
`{ } |`: align commnads, left right center, respectively.

`dc`: remove a column
`yr`: yank a row
`9yr`: yank nine rows

`ccopy`: copy to clipboard
`cpaste`: paste from clipboard

Regarding pasting content adapting cell references, 
you should yank with normal 'y' and then you should paste content with 'Pc'..

Default color:
WHITE, BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN

cellcolor A2:A6 "bg=WHITE fg=CYAN bold=1 underline=1 italic=1""

Freeze
fc : freeze column
fr : freeze row

Paste numerical functions
1. Pc
2. yank and enter into a  visual mode and then paste

Search:
/"Text"
/3

e 	Edit a numeric value
E 	Edit a string value
x 	Delete current cell content
:q 	Quit the app
:h 	See help
:w filename.sc 	Save current spreadsheet in sc format
j 	Move down
k 	Move up
h 	Move left
l 	Move right
goab12 	go to cell AB12
u 	undo last change
C-r 	redo last change undone
yy 	Copy current cell
v 	select a range using cursor/hjkl keys
p 	paste a previously yanked cell or range
ir 	insert row
ic 	insert column
dr 	delete row
dc 	delete column
