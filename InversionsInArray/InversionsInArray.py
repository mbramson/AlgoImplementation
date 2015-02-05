# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 22:35:50 2015

@author: Bramson

This is an implementation of the divide and conquer paradigm applied to the
problem of counting inversions in an array.

The idea was to implement a solution in python that does not make use of any
global variables and that is as readable as possible.

This was accomplished by "hiding" the running count in the first element of
the array returned by the merge function. This is why the indexes i and j
both start at 1 instead of 0. They have to ignore the first element as that
is the running count. This is also why the running count, c, is instantiated
as the sum of the first elements of the left and right lists.

Other than that, this runs like a standard mergesort based Inversion Counter.
It is verbose for clarity.

This will run in O(n logn) time.

"""

## This is the helper method of InversionCount and the main recursive method.
## It returns a list where the first element is the number of inversions in
## li. The other elements are simply sorted li.
def merge(li):
    if len(li) < 2:
        return [0] + li ## There are no inversions in a single element array
    h = len(li) / 2 ##Halfway point used to recursively divide the list
    left = merge(li[:h])
    right = merge(li[h:])
    c = left[0] + right[0] ##1st elements of lists are their inversion counts
    i = j = 1 ##Must ignore 1st element of left and right.
    returnlist = []
    ## Following loop counts split inversions and sorts the entire array
    for i in range(len(li)):  ## This could easily be    "while(True):"
        if i == len(left):
            returnlist.extend(right[j:])
            break
        if j == len(right):
            returnlist.extend(left[i:])
            break
        if left[i] <= right[j]:
            returnlist.append(left[i])
            i += 1
            continue
        else:
            returnlist.append(right[i])
            j += 1
            c += len(left[i:])
            continue
    return [c] + returnlist ## Append running count to beginning of array

## This method simply returns the first element of the merge function, which is
## The total number of inversions in li     
def InversionCount(li):
    return merge(li)[0]