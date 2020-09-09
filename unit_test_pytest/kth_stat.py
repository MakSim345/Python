#!/usr/bin/env python
import random

def kth_stat(iterable, k):
    """ return [k-1] item from the list """
    print "kth_stat iterable: ", iterable
    print "kth_stat K: ", k
    print "sorted:", sorted(iterable)
    # assert isinstance(iterable, Iterable), "expected iterable as first argument"
    assert k > 0, "k should be non-zero positive number"
    return sorted (iterable) [k - 1]

# main entrance point:
if __name__ == "__main__":
    a = (list(range(10)))
    random.shuffle(a)
    print "randomized a =", a
    print kth_stat(a, 3)
