#!/usr/bin/python
"""
Program to find word frequency
Author: Shruti Thakkar
Version: V1
"""
import sys

def word_freq(filename):
    """
        Count frequency of word
    """
    with open(filename, "r") as file_handle:
        file_line = file_handle.read()
        word_list = file_line.split()
        dic_word = {}
        for i in word_list:
            dic_word[i] = word_list.count(i)
        return dic_word

def word_count(filename):
    """
       count number of word
    """
    with open(filename, "r") as file_handle:
        file_line = file_handle.read()
        word_list = file_line.split()
        count = len(word_list)
    return count

def main():
    """
      Main
    """
    count_word = word_count(sys.argv[1])
    print "Total number of words in file %s is %d" % (sys.argv[1], count_word)

    out = word_freq(sys.argv[1])
    for print_word in out:
        print print_word, out[print_word]

main()
