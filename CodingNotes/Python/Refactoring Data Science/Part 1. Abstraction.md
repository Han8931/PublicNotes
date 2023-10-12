
# Tracker
```python
from enum import Enum, auto
from pathlib import Path
from typing import Protocol
import numpy as np

class Stage(Enum):
    TRAIN = auto()
    TEST = auto()
    VAL = auto()

class ExperimentTracker(Protocol):
    def set_stage(self, stage: Stage):
        """Sets the current stage of the experiment."""

    def add_batch_metric(self, name: str, value: float, step: int):
        """Implements logging a batch-level metric."""

    def add_epoch_metric(self, name: str, value: float, step: int):
        """Implements logging a epoch-level metric."""

    def add_epoch_confusion_matrix(
        self, y_true: list[np.array], y_pred: list[np.array], step: int
    ):
        """Implements logging a confusion matrix at epoch-level."""

```

# Function Composition

```python
class LinearNet(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.network = torch.nn.Sequential(
            torch.nn.Flatten(),
            torch.nn.Linear(in_features=28 * 28, out_features=32),
            torch.nn.ReLU(),
            torch.nn.Linear(in_features=32, out_features=10),
            torch.nn.Softmax(dim=1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)
```

```python
import functools
from typing import Callable

ComposableFunction = Callable[[float], float]

def compose(*functions: ComposableFunction)->ComposableFunction:
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)

def addThree(x:float)->float:
    return x+3

def multiplyByTwo(x: float)->float:
    return x*2

def main():
    x = 12
    myfunc = compose(addThree, addThree, multiplyByTwo, multiplyByTwo)
    result = myfunc(x)
    print(f"Result: {x}") 

if __name__ == "__main__":
    main()
```