#!/usr/bin/python3
'''Pascal's triangle representation
'''

def pascal_triangle(n):
    '''returns a list of integers representing the pascal's triangle of a given
    number

    Args:
        n (integer): the given number

    Return:
        return a list of integers
    '''

    nlist = []

    if (n <= 0):
        return nlist

    nlist.append([1])

    for i in range(n - 1):
        nlist.append([1] + [nlist[i][j] + nlist[i][j + 1]
                            for j in range(len(nlist[i]) - 1)] + [1])

    return nlist
