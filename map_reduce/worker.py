from dataclasses import dataclass
from map_reduce.tasks import MapTask, ReduceTask


@dataclass
class Worker:
    """
    The Worker processes a task the Driver has created.
    It produces a set of output files with the word counts of all words
    appearing in any of the input files.
    (Driver and Workers only communicate over REST, have direct access to the
    local file system, and can be started separately.)
    """
    
    def map_(self) -> float:
        """Description..."""
        # TODO
        # take the input files, separate text into single words,
        # and put each word into a "bucket" (an intermediate file)
        # see documentation...
        print("Worker.map_()...")


    def reduce_(self) -> float:
        """Description..."""
        # TODO
        # take all mr-<map task id>-<bucket id> files with bucket id = reduce task id,
        # count the frequency of each word,
        # and output a final file out-<reduce task id>
        # see documentation...
        print("Worker.reduce_()...")
    
    
    def run(self):
        """Description..."""
        # TODO
        # self.map_()...
        # self.reduce_()...
        print("Worker.run()...")
        
    
    # Worker should also be able to know when Driver has finished,
    # and finish itself as well...
