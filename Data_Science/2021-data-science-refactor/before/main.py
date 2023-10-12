from os import path
import torch
import pathlib

from src.dataset import get_train_dataloader, get_test_dataloader
from src.models import LinearNet

from src.running import Runner, run_epoch
from src.tracking import Stage
from src.tensorboard import TensorboardExperiment
from src.utils import generate_tensorboard_experiment_directory

# Hyperparameters
EPOCH_COUNT = 20
LR = 5e-5
BATCH_SIZE = 128
LOG_PATH = "./runs"

# Data configuration
DATA_DIR = "./data"
TEST_DATA = pathlib.Path(f"{DATA_DIR}/t10k-images-idx3-ubyte.gz")
TEST_LABELS = pathlib.Path(f"{DATA_DIR}/t10k-labels-idx1-ubyte.gz")
TRAIN_DATA = pathlib.Path(f"{DATA_DIR}/train-images-idx3-ubyte.gz")
TRAIN_LABELS = pathlib.Path(f"{DATA_DIR}/train-labels-idx1-ubyte.gz")


def main():
    # Data
    train_loader = get_train_dataloader(batch_size=BATCH_SIZE)
    test_loader = get_test_dataloader(batch_size=BATCH_SIZE)

    # Model and Optimizer
    model = LinearNet()
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    # Create the runners
    test_runner = Runner(test_loader, model)
    train_runner = Runner(train_loader, model, optimizer)

    # Experiment Trackers
    experiment = TensorboardExperiment(log_dir=LOG_PATH)

    for epoch_id in range(EPOCH_COUNT):
        run_epoch(test_runner, train_runner, experiment, epoch_id, EPOCH_COUNT)

    experiment.flush()

if __name__ == "__main__":
    main()
