#!/usr/bin/env python

from argparse import ArgumentParser
from itertools import combinations
from math import sqrt, factorial

iterations= 0

def delta(y, X):

    diff= []
 
    for xi in X:
        diff.append(abs(y - xi))

    return diff

def process_delta(y, D, X, L, width):

    # if delta(y, X) is subset of L
    if set(D).issubset( L ):
     
        # Add y to X and remove lengths delta(y, X) from L
        X.append(y)
        map(L.remove, D)

        # PLACE(L,X)
        place(L, X, width)
    
        # Remove y from X and add lengths delta(y, X) to L 
        if y in X:
            X.remove(y)
        L.extend(D)


def place(L, X, width):

    global iterations
    iterations+= 1

    # if L is empty
    if not L:

        # output X
        print 'X = %s in %i iterations' % (sorted(X), iterations)

        return 

    # y <- maximum element in L
    y= max(L)

    # outer most distance y
    D= delta(y, X)
    process_delta(y, D, X, L, width)
  
    # second outer most distance abs(width - y)
    y= abs(width - y)
    D= delta(y, X)
    process_delta(y, D, X, L, width)

    # backtrack
    return
  
def partial_digest(L):

    # width <- Maximum element in L
    width= max(L)

    # DELETE (width, L)
    L.remove(width)
   
    # X <- {0, width}
    X= [0, width]

    # PLACE(L, X, width)
    place(L, X, width)

    return 

if __name__ == '__main__':
    """              (n)
    """

    parser= ArgumentParser(description= 'Partial Digest Problem')
    parser.add_argument('--L', type= int, nargs= '+', default= [2,2,3,3,4,5,6,7,8,10], help= 'list of integers')

    args= parser.parse_args()
    L= args.L

    global iterations
    iterations= 0

    print "L = %s" % (L)

    partial_digest(L)

