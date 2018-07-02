#!/usr/bin/env python

from time import time
from argparse import ArgumentParser
from itertools import combinations
from math import sqrt, factorial


def dX_from_X(X):
    """
    Forms delta-X by computing the differences
    between all elements of X:
        dX = {Xj - Xi : 1 <= i < j <= n}
    """

    dX= []

    for i in range(len(X) - 1):
        for j in range(i+1, len(X)):
            dX.append(X[j] - X[i])
    dX.sort()

    return dX

def brute_force(L, n, optimization= True):
    """
    M <- maximum eleent in L
    for every set of n-2 integers 0 < X2 < ... < Xn-1 < M
        X <- {0, X2, ..., Xn-1, M}
        Form dX from X
        if dX = L
            return X
    output "No Solution"
    """

    # M <- maximum element in L
    M = max(L)

    if optimization:
        # for every set if n-2 integers 0 < X2 < ... < Xn-1 < M from L 
        sets= list(combinations(L, n-2))
    else:
        # for every set if n-2 integers 0 < X2 < ... < Xn-1 < M
        sets= list(combinations(range(0, M), n-2))

    iterations= 0
    for X in sets:

        # X <- {0, X[2],...X[n-1], M}
        X = [0] + sorted(X) + [M]

        # Form delta-X from X
        dX= dX_from_X(X)

        # if dX = L
        if (dX == L):
            return (X, iterations)

        iterations+= 1

    # No Solution
    return (None, iterations)


if __name__ == '__main__':
    """              (n)
    Given a multiset | | of positve numbers dX, does there
                     (2)
    exist a set X such that dX is exactly the multiset of all
    positive pairwise differences of the elements of X.
    """

    parser= ArgumentParser(description= 'Partial Digest Problem')
    parser.add_argument('--optimization', dest= 'optimization', action= 'store_true', default= False, help= "Turn on optmization")
    parser.add_argument('--L', type= int, nargs= '+', default= [2,2,3,3,4,5,6,7,8,10], help= 'list of integers')

    args= parser.parse_args()
    print args
    optimization= args.optimization
    L= args.L

    print "L = %s" % (L)

    """
        (n/k) = "n choose k"

                   n!
        (n/k) = -------- = the number of distinct subsets of 
                (n-k)!k!   k elements from a set of n elements.

                n * (n-1)
        (n/k) = --------- = the number of dffferent pairs 
                   2        of elements from an n-element set.

         n                      n * (n-1)
         E Xi = X1+X2+X3...Xn = --------- 
        i=0                        2     

           (sqrt(1 + 8 * n) + 1)
        n= ---------------------
                    2

    """

    n = int( (sqrt(1 + 8 * len(L)) + 1) / 2 )

    start_time= time()
    (X, iterations) = brute_force(L, n, optimization)
    end_time= time()

    output= "X = %s" % (X) if X else "No Solution"
    print "%s in %s iterations" % (output, iterations)
    print end_time - start_time, "seconds"
