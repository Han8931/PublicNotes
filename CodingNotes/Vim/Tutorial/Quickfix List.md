When we run the `:make` command, Vim automatically jumps to the first error (unless there are none). If we prefer that our cursor remain where it is, we can instead run this:
`$ make!`

The trailing `!` character tells Vim to update the quickfix list without jumping to the first item. Now suppose that we run `:make` and immediately realize that we should have used the bang version. How can we get back to where we were before we ran `:make`? Simple: use the `<C-o>` command to jump back to the previous position in the jump list. See Tip 55, on page 131, for more details.

`:cnext` Jump to next item
`:cprev` Jump to previous item
`:cfirst` Jump to first item
`:clast` Jump to last item
`:cnfile` Jump to first item in next file
`:cpfile` Jump to last item in previous file
`:cc` N Jump to nth item
`:copen` Open the quickfix window
`:cclose` Close the quickfix window

