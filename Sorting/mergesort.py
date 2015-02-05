# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 09:45:37 2015

@author: Bramson
"""

##This function sorts an array of elements, li, recursively using the mergesort algorithm.
def mergesort(li):
    if len(li) <= 1:
        return li
    left =  mergesort(li[0:len(li)/2])
    right = mergesort(li[len(li)/2:])
    returnlist = []
    while (True):
        if len(left) == 0:
            returnlist += right
            break
        if len(right) == 0:
            returnlist += left
            break
        if left[0] <= right[0]:
            returnlist.append(left.pop(0))
        else:
            returnlist.append(right.pop(0))
    return returnlist