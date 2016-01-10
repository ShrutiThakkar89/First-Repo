#!/usr/bin/python
import sys

def word_freq(filename):
    with open (filename, "r") as f:
        s = f.read()
        word_list = s.split()
        d = {}
        for i in word_list:
             d[i] = word_list.count(i)
        return d

def word_count(filename):
    with open (filename, "r") as f:
        s = f.read()
        word_list = s.split()
        count = len(word_list)
    
    return count

c = word_count(sys.argv[1]) 
print "Total number of words in file %s is %d" % (sys.argv[1], c)

o_d = word_freq(sys.argv[1])
for p in o_d:
    print p, o_d[p]
