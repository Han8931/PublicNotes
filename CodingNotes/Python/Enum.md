`Enum` is a way that Python enumerate variables. 
```python
from enum import Enum

class State(Enum):
	PLAYING=0
	PAUSED=1
	GAME_OVER=2
```

If we just want to make sure them to be unique and automatically assigned, then use `auto()`
```python
from enum import Enum, auto

class State(Enum):
	PLAYING=auto()
	PAUSED=auto()
	GAME_OVER=auto()

print(State.PLAYING)
print(State.PLAYING.value)
```

Or simply, 

```python
from enum import Enum, auto

class State(Enum):
	PLAYING, PAUSED, GAME_OVER=range(3)

print(State.PLAYING)
print(State.PLAYING.value)
```

However, this hard codes numbers, which can create an issue in the future.  It would be better to use strings to initialize them. 

```python
from enum import Enum, auto

class State(Enum):
	PLAYING="playing"
	PAUSED="paused"
	GAME_OVER="game_over"

print(State.PLAYING)
print(State.PLAYING.value)
```