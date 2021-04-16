import collections
import numpy as np


class RunningStats():
    """
    Class to hold data that matures after a given number of updates.
    """

    def __init__(self, len) -> None:
        super().__init__()
        self.queue = collections.deque(maxlen=len)
    

    def append(self, x):
        self.queue.append(x)
    

    def stats_using(self, fn, **kwargs):
        """
        Compute the statistics using a given function.
        """
        return fn(np.array(self.queue), **kwargs)

    
    def mean(self, **kwargs):
        return self.stats_using(np.mean, **kwargs)
    

    def std(self, **kwargs):
        return self.stats_using(np.std, **kwargs)