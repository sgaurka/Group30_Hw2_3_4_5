from Cols import Cols
from Row import Row
from csv_parser import csv
from Cols import Cols
from Row import Row

class Data:
    
    def __init__(self, src):
        self.src = src
        self.cols = None
        self.rows = {}
        self.create()
        
    def create(self):
        if (type(self.src) == str):
            csv(self.src, self.add)
        else:
            for _, row in enumerate(self.src or {}):
                self.add(row)
       
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            try:
                self.rows.append(xs.cells)
            except:
                self.rows.append(Row(xs))
            row=self.rows
            for todo in self.cols.x+self.cols.y:
                for col in todo:
                    col.add(row.cells[col.at])
     
    def stats(self, places, showCols, fun):
        t={}
        if showCols==None:
            showCols=self.cols.y
        if fun==None:
            fun="mid"
        for col in showCols:
            v=fun(col)
            if type(v)==int or type(v)==float:
                v=round(v,places)
            t[col.name]=v
        return t
            
     
if __name__ == '__main__':
    data = Data("./../data/auto93.csv")
    print(data.rows)
    print(data.cols)
        
