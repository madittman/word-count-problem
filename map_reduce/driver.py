import os
import http.server
import socketserver
from dataclasses import dataclass, field
from typing import List
from map_reduce.tasks import MapTask, ReduceTask


@dataclass
class Driver:
    """
    The Driver divides the total work among different tasks so that a number of
    independent Workers process these tasks until completion.
    (Driver and Workers only communicate over REST, have direct access to the
    local file system, and can be started separately.)
    """
    num_of_map_tasks: int
    num_of_reduce_tasks: int
    path: str  # path of input files
    all_files: List[str] = field(init=False)  # list of files depends on path

    def __post_init__(self):
        self.all_files = os.listdir(self.path)
        
    
    def _divide_files(self) -> List[List[str]]:
        """
        Divide files among MapTasks and return list of file lists per MapTask.
        """
        files_per_map_task: List[List[str]] = []
        num_of_all_files = len(self.all_files)
        
        # step is number of files per map task
        step = num_of_all_files / self.num_of_map_tasks
        result_is_uneven = bool(step % 1)  # true if step is a decimal
        
        start = 0
        step = int(step)  # remove decimals
        for i in range(self.num_of_map_tasks):
            stop = start + step
            files_per_map_task.append(self.all_files[start:stop])
            start = stop
            
            if result_is_uneven:  # step hasn't come out even
                # So check if remaining files can be divided among remaining
                # map tasks by increasing the step by 1.
                remaining_files = self.all_files[start:]
                num_of_remaining_map_tasks = self.num_of_map_tasks - (i+1)
                if not len(remaining_files) % num_of_remaining_map_tasks:
                    step += 1  # increase step by 1 to come out even
                    result_is_uneven = False  # make sure this is only run once

        return files_per_map_task
        
    
    def _create_tasks(self):
        """Create all MapTasks and ReduceTasks."""
        files_per_map_task = self._divide_files()
        
        map_tasks = List[MapTask]
        for map_task_id in range(self.num_of_map_tasks):
            map_tasks.append(
                MapTask(
                    task_id=map_task_id,
                    # take subset of input files
                    files=files_per_map_task[map_task_id],
                )
            )
        
        reduce_tasks = List[ReduceTask]
        for reduce_task_id in range(self.num_of_reduce_tasks):
            reduce_tasks.append(
                ReduceTask(
                    task_id=reduce_task_id,
                    files=[],  # TODO: repair
                )
            )


    def start(self):
        """Divide input files between different Workers."""
        
        # TODO: set up server...
        print("Driver.start()...")


    # The Driver should be able to decide when all tasks have finished,
    # and then exit...
