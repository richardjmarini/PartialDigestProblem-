#!/usr/bin/env python

from sys import exit, stderr
from argparse import ArgumentParser
from math import sqrt

from bruteforce import brute_force
from practical_bruteforce import partial_digest

if __name__ == '__main__':

    parser= ArgumentParser(description= 'Partial Digest Problem')
    parser.add_argument('--optimization', type= int, default= 0, help= "sets optimization level [0= bruteforce, 1= optimized_brute_force, 2= practical_brute_force]")
    parser.add_argument('--L', type= int, nargs= '+', default= [2,2,3,3,4,5,6,7,8,10], help= 'list of integers')


    args= parser.parse_args()
    optimization_level= args.optimization
    L= args.L

    print "Optmization Level: %s" % (optimization_level)
    print "L= %s" % (L)

    if optimization_level in (0, 1):

        n = int( (sqrt(1 + 8 * len(L)) + 1) / 2 )

        (X, iterations) = brute_force(L, n, optimization_level)

        output= "X = %s" % (X) if X else "No Solution"
        print "%s in %s iterations" % (output, iterations)

    elif optimization_level == 2:

        partial_digest(L)

    else:
        print >> stderr, "invalid optimization level"
        exit(-1)
