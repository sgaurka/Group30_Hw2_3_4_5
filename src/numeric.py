from csv_parser import the
import math
import random

class Num:
  def __init__(self,c=0,s=""):
    self.n=0
    self.at=c
    self.name=s
    self._has=[]
    self.lo=math.inf
    self.hi=-math.inf
    self.isSorted=True
    if(s==""):
      w=0
    elif(s[-1]=='+'):
      w=1
    elif(s[-1]=='-'):
      w=-1
    else:
      w=0
  
  def nums(self):
    if self.isSorted==False:
      self._has.sort()
      self.isSorted=True
    return self._has
  
  def add (self, v, nums): 
      if v!="?":
          self.n += 1
          if self.lo > v:  
              self.lo=v
          if self.hi < v: 
              self.hi=v
          if len(self._has) < nums: 
              pos=len(self._has)
          elif random.uniform(0, 1) < nums/self.n:
              pos=random.randint(0, len(self._has) - 1)               
          if 'pos' in locals(): 
              self.isSorted=False
              if pos < len(self._has):
                  self._has[pos]=float(v) 
              else:
                  self._has.insert(pos, float(v)) 
          return
        
  def div(self):
    a=self.nums()
    index_90th=int(len(a)*0.9)
    index_10th=int(len(a)*0.1)
    return (a[index_90th]-a[index_10th])/2.58
    
  def mid(self):
    a=self.nums()
    index_50th=int(len(a)*0.5)
    return a[index_50th]
