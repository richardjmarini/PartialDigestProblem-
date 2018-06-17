#!/usr/bin/env python

from argparse import ArgumentParser
from itertools import combinations
from math import sqrt, factorial
from copy import copy

iterations= 0

def process_delta(y, D, X, L, width, solutions):

    # if delta(y, X) is subset of L
    if set(D).issubset( L ):
     
        # Add y to X and remove lengths delta(y, X) from L
        X.append(y)
        [L.remove(d) for d in D if d in L]

        # PLACE(L,X)
        place(L, X, width, solutions)
   
        # replaced by copy() prior to call to process_delta()
        # Remove y from X and add lengths delta(y, X) to L 
        #X.remove(y) # undo modifications to X for next recursive call
        #L.extend(D) # undo modifications to L for the next recursrive call

    return 


def place(L, X, width, solutions):
  
    global iterations
    iterations+= 1

    # if L is empty
    if not L:

        # output X
        solutions.append((X, iterations))
        return 

    # y <- maximum element in L
    y= max(L)

    # outer most distance y
    D= [abs(y - x) for x in X]
    process_delta(y, D, copy(X), copy(L), width, solutions)
  
    # second outer most distance abs(width - y)
    y= abs(width - y)
    D= [abs(y - x) for x in X]
    process_delta(y, D, copy(X), copy(L), width, solutions)
   
    # backtrack
    return
  
def partial_digest(L, solutions= []):

    # width <- Maximum element in L
    width= max(L)

    # DELETE (width, L)
    L.remove(width)
   
    # X <- {0, width}
    X= [0, width]

    # PLACE(L, X, width)
    place(L, X, width, solutions)

    return 

if __name__ == '__main__':
    
    parser= ArgumentParser(description= 'Partial Digest Problem')
    parser.add_argument('--L', type= int, nargs= '+', default= [2,2,3,3,4,5,6,7,8,10], help= 'list of integers')

    args= parser.parse_args()
    L= args.L

    solutions= []

    print "L = %s" % (L)

    partial_digest(L, solutions)
    
    for (X, iterations) in solutions:
        print 'X = %s in %i iterations' % (X, iterations)

