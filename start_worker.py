import requests
from map_reduce.worker import Worker


# set up Worker
worker = Worker()

# waiting for Driver...
# ask Driver for concrete task...

worker.run()  # TODO: check if Driver has finished

print("Worker has finished")
