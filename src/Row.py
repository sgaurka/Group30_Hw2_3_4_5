import math
from csv_parser import copy 

#Row class creates non mutable copies of values from a given dictionary
class Row:
    cells = {}
    cooked = {}
    isEvaled = False

    def __init__(self, t):
        if t:
            self.cells = t
        self.cooked = copy(t)
        self.isEvaled = False
       
if __name__ == '__main__':
    row = Row({2:3,4:5})
    
