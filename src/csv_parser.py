import re
import sys

the = {}
separator = ','
help='''
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license

USAGE: lua seen.lua [OPTIONS]

OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --seperator feild seperator                       = , 
'''

"""
Functions to handle settings
"""
# Try to convert string to number
def toNumber(s):
    try:
        intValue = int(s)
        return intValue
    except ValueError:
        return False
        
# Parse `the` config settings from `help`.
def coerce(s):
    def fun(s1):
        if s1 == 'true':
            return True
        if s1 == 'false':
            return False
        return s1
    regex = re.compile(r'\s*(.+)\s*')
    res = regex.search(s)
    return toNumber(s) or fun(res.groups()[0])

# Work In Progress: 
# Update settings from values on command-line flags. Booleans need no values (we just flip the defeaults).
def cli(t, args):
    print(t, args)
    for slot,v in t.items():
        print (slot, v)
# creates a non mutable copy of a dictionary
def copy(t):
    if type(t)!=dict:
        return t
    u ={}
    for key, value in t.items():
        u[key] = copy(value)
    return u
    
# Create a 'the' variable
def createDefaultTheFromHelp():
    regex = re.compile(r'\s-([A-Za-z])+\s+--(\w+)\s+.+[\s]+=\s(.+)')

    for string in help.split('\n'):
        res = regex.search(string)
        if res:
            _, k, x = res.groups()
            the[k] = coerce(x.strip())

# Read CSV file
def csv(filename, fun):
    with open(filename, 'r') as csv_file:
        lines = csv_file.readlines()
        t = {} 
        for line in lines:
            arr = line.strip().split(the.separator)
            t[1 + len(t)] = coerce(arr)
        fun(t)
    csv_file.close()
    
if __name__ == '__main__':
    args = sys.argv
    createDefaultTheFromHelp()
    the = cli(the, args)
