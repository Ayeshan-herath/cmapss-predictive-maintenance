
from pathlib import Path
from zipfile import ZipFile
import pandas as pd


COLUMNS = (
    ["engine_id", "cycle"]
    + [f"setting_{i}" for i in range(1, 4)]
    + [f"sensor_{i}" for i in range(1, 22)]
)


def load_fd001(zip_path):
    """
    Load the NASA C-MAPSS FD001 dataset.

    Returns:
        train_df: Training engine histories
        test_df: Test engine histories
        rul_df: True RUL values for test engines
    """

    zip_path = Path(zip_path)

    with ZipFile(zip_path, "r") as archive:

        with archive.open("train_FD001.txt") as file:
            train_df = pd.read_csv(
                file,
                sep=r"\s+",
                header=None,
                names=COLUMNS
            )

        with archive.open("test_FD001.txt") as file:
            test_df = pd.read_csv(
                file,
                sep=r"\s+",
                header=None,
                names=COLUMNS
            )

        with archive.open("RUL_FD001.txt") as file:
            rul_df = pd.read_csv(
                file,
                sep=r"\s+",
                header=None,
                names=["RUL"]
            )

    return train_df, test_df, rul_df
