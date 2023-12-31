# from abc import ABC, abstractmethod
# from dataclasses import dataclass
from pathlib import Path
from typing import Union, Tuple

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from torch.utils.tensorboard import SummaryWriter
from enum import Enum, auto
from typing import Protocol


# @dataclass(frozen=True)
# class Stage:
#     TRAIN: str = 'train'
#     TEST: str = 'test'
#     VAL: str = 'val'

class Stage(Enum):
    TRAIN = auto()
    TEST = auto()
    VAL = auto()


class ExperimentTracker(Protocol):

    def add_batch_metric(self, name: str, value: float, step: int):
        """Implements logging a batch-level metric."""

    def add_epoch_metric(self, name: str, value: float, step: int):
        """Implements logging a epoch-level metric."""

    def add_epoch_confusion_matrix(self, y_true: np.array, y_pred: np.array, step: int):
        """Implements logging a confusion matrix at epoch-level."""

    def add_hparams(self, hparams: dict[str, Union[str, float]], metrics: dict[str, float]):
        """Implements logging hyperparameters."""

    def set_stage(self, stage: Stage):
        """Sets the stage of the experiment."""

    def flush(self):
        """Flushes the experiment."""

    # def add_batch_metrics(self, values: dict[str, float], step: int):
    #     for name, value in values.items():
    #         self.add_batch_metric(name, value, step)

    # def add_epoch_metrics(self, values: dict[str, float], step: int):
    #     for name, value in values.items():
    #         self.add_epoch_metric(name, value, step)


