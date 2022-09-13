import math
import copy from csv_parser

class Row:
    cells = {}
    cooked = 0
    isEvaled = false

    def __init__(self, t):
        if t:
            self.cells = t
        self.cooked = copy(t)
        self.isEvaled = false
        
