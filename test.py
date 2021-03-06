#!/usr/bin/env python

from math import sqrt
from bruteforce import brute_force
from practical_bruteforce import partial_digest


import unittest

class TestStringMethods(unittest.TestCase):

    TEST_DIGESTS= {
        (2,2,3,3,4,5,6,7,8,10): (
            (0, 3, 6, 8, 10),
            (0, 2, 4, 7, 10)             
        ),
        (1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,6,6,7,7,8,8,8,9,9,10,10,11,11,12,12,12,13,14,15): (
            (0,2,3,8,10,11,12,14,15),
            (0,2,3,4,6,7,12,14,15),
            (0,1,3,8,9,11,12,13,15),
            (0,1,3,4,5,7,12,13,15),
        ),
        (1,2,2,2,3,3,3,4,5,5,5,6,7,8,10): (
            (0,3,5,6,8,10),
            (0,2,4,5,7,10)
        ),
        (1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,9,9,10,11,12,15): (
            (0,6,9,10,11,12,15),
            (0,3,4,5,6,9,15)
        )

    }

    def test_brute_force(self):

        print 'brute force...'

        for (L, solutions) in self.TEST_DIGESTS.items():

            print "L=", L

            n = int( (sqrt(1 + 8 * len(L)) + 1) / 2 ) 
            (solution, iterations) = brute_force(list(L), n, 0)
            print 'found %s in %i iterations' % (solution, iterations)
            self.assertTrue(tuple(solution) in solutions)

    def test_brute_force_optmiization(self):

        print 'brute force optimized...'

        for (L, solutions) in self.TEST_DIGESTS.items():

            print "L=", L

            n = int( (sqrt(1 + 8 * len(L)) + 1) / 2 ) 
            (solution, iterations) = brute_force(list(L), n, 1)
            print 'found %s in %i iterations' % (solution, iterations)
            self.assertTrue(tuple(solution) in solutions)

    def test_practical_brute_force(self):

        print 'practical brute force...'

        for (L, solutions) in self.TEST_DIGESTS.items():

            print "L=", L

            results= []
            partial_digest(list(L), results)
            for (solution, iterations) in results: 
                print 'found %s in %i iterations' % (solution, iterations)
                self.assertTrue(tuple(solution) in solutions)



if __name__ == '__main__':

    unittest.main()
