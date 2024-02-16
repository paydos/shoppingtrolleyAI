from core.supermarket_objects import Aisle
from settings.paths import stock_path

import json
import numpy as np
import shutil


class Supermarket:

    def __init__(self, size: np.array) -> None:
        self.aisles = {}
        
        self.size = size
        self.empty_layout = np.zeros(size)
        with open(stock_path, 'r') as file:
            self.stock = json.load(file)
    
    
    
    
    
    def add_aisle(self, aisle: Aisle):
        self.aisles[aisle.name] = aisle
        self._update_layout(aisle)
        
    def _update_layout(self, aisle: Aisle):
        y, x = eval(aisle.location)
        length = aisle.length
        self.empty_layout[x:x+length, y] = 1
        
        
    
    
    
    def show_layout(self):
        layout_str = np.array2string(self.empty_layout, threshold=np.inf, separator='', formatter={'all':lambda x: '⬛' if int(x) == 1 else '⬜'})
        layout_lines = layout_str.split('\n')
        max_line_length = max(len(line) for line in layout_lines)
        console_width = shutil.get_terminal_size((80, 20)).columns
        if max_line_length < console_width:
            padding = (console_width - max_line_length) // 2
            padded_layout = '\n'.join(' ' * padding + line for line in layout_lines)
            print(padded_layout)
        else:
            print(layout_str)
