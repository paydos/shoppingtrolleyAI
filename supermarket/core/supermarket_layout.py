from core.supermarket_objects import Aisle
import numpy as np

class Supermarket:

    def __init__(self, size: np.array) -> None:
        self.aisles = {}
        
        self.size = size
        self.empty_layout = np.zeros(size)
        
    
    
    
    
    
    def add_aisle(self, aisle: Aisle):
        self.aisles[aisle.name] = aisle
        self._update_layout(aisle)
        
        
    def _update_layout(self, aisle: Aisle):
        x, y = eval(aisle.location)
        length = aisle.length
        self.empty_layout[x, y:y+length] = 1
        
    
    
    
    
    def show_layout(self):
        with np.printoptions(threshold=np.inf):
            print(self.empty_layout)

