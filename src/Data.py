from csv_parser import csv

class Data:
    
    def __init__(self, src):
        self.src = src
        self.cols = None
        self.rows = {}
        
    def create(self):
       csv(self.src, self.add)
       
    def add(self, xs):
        if len(self.cols) == 0:
            self.cols = Col(xs)
        # TODO: else
            
     
if __name__ == '__main__':
    data = Data("./../data/auto93.csv")
    print(data)
        