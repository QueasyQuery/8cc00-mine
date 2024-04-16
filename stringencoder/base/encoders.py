from .base_encoder import BaseStringEncoder
import numpy as np

class OneHotEncoder(BaseStringEncoder):

    def __init__(self, table: str = 'helo', **kwargs):
        self._mat = np.eye(len(table))
        super().__init__(table, self._mat, **kwargs)
    
    def __str__(self):
        return self.__class__.__name__ + str(self._kwargs)
    
    def __repr__(self):
        return self.__str__()


