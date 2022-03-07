from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    """Class for defining a general Task object."""
    task_id: int
    files: List[str]  # list of input files for task


@dataclass
class MapTask(Task):
    """Class for defining MapTask."""
    # TODO
    pass


@dataclass
class ReduceTask(Task):
    """Class for defining ReduceTask."""
    # TODO
    pass
