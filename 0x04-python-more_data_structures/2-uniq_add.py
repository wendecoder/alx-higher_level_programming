#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumation = 0
    for i in set(my_list):
        sumation += i
    return sumation
