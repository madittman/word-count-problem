import argparse
from map_reduce.driver import Driver
from map_reduce.tasks import MapTask, ReduceTask


# TODO
# input num of map_tasks...
# input num of reduce_tasks...
num_of_map_tasks = 6
num_of_reduce_tasks = 4
path = "map_reduce/_inputs"

# set up Driver
# (Driver doesn't know how many Workers will show up)
driver = Driver(
    num_of_map_tasks=num_of_map_tasks,
    num_of_reduce_tasks=num_of_reduce_tasks,
    path=path,
)
driver.start()  # TODO: listen for worker and assign task...

# Driver has finished
print("Driver has finished")
# TODO: send signal to workers...
