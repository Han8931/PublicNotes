(C-b %): split window vertically
(C-b ")	: split window horizontally
(C-b arrow): move around the splitted window
(C-b ( ): Move to previous session
(C-b ) ): Move to next session

(C-d):close window

(Alt-character): move to session


(C-b L)		: Switch to the last active session


(C-b [)         :Scroll

(C-b :)		:Command mode

Resizing	:
		:resize-pane -D (Resizes the current pane down)
		:resize-pane -U (Resizes the current pane upward)
		:resize-pane -L (Resizes the current pane left)
		:resize-pane -R (Resizes the current pane right)
		:resize-pane -D 10 (Resizes the current pane down by 10 cells)
		:resize-pane -U 10 (Resizes the current pane upward by 10 cells)
		:resize-pane -L 10 (Resizes the current pane left by 10 cells)
		:resize-pane -R 10 (Resizes the current pane right by 10 cells) 

(C-b d)		:Detach 
(C-b s)         :Switch to another session

(C-b $) myname	:Rename session name: 

start new:
tmux

start new with session name:
tmux new -s myname
tmux new-session -s [name]

Rename session:
tmux rename-session [-t current-name] [new-name]

Rename current session:
tmux rename-session [new-name]


attach to named:
tmux a -t myname or number

list sessions:
tmux ls

kill session:
tmux kill-session -t myname

