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
  
  def add(self,v):
    if v!='?':
      self.n=self.n+1
      self.lo=min(self.lo,v)
      self.hi=max(self.hi,v)
      if len(self._has)<the['nums']:
        pos=1+len(self._has)
        self._has.append(v)
      elif random.random()<the['nums']/self.n:
        pos=random.randint(0,the['nums']-1)
        self._has[pos]=v
      else:
        pos=-1
      if pos!=-1:
        self.isSorted=False
