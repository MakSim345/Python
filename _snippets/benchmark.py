#!/usr/bin/env python

# test whether a number is a power of 2
# and a benchmark.

import random
import datetime
import math
import time
# from datetime import datetime


def check2rec(num):
    ''' use recursion'''
    if num == 1:
        return True
    if num & 1:
        return False
    return check2rec(num >> 1)

def check2log(num):
    '''use logarithms '''
    r = math.log(num, 2)
    return int(r) == r

def is_power2(num):
	'''states if a number is a power of two'''
	return num != 0 and ((num & (num - 1)) == 0)

def run_benchmark(max_rnd_numbers=1000):
    '''run 3 different functions and check time taken to calculate for each.'''
    numbers = list()
    print('Generating numbers...')
    for _ in range(max_rnd_numbers):
        numbers.append(random.randint(10000, 1000000))
    print('Done!')

    start = datetime.datetime.now()
    for _ in range(10000):
        for n in numbers:
            check2rec(n)
    print('Recursion way takes: ', datetime.datetime.now() - start)

    start = datetime.datetime.now()
    for _ in range(10000):
        for n in numbers:
            check2log(n)
    print('Logarithms way takes: ', datetime.datetime.now() - start)

    start = datetime.datetime.now()
    for _ in range(10000):
        for n in numbers:
            is_power2(n)
    print('Binary_AND way takes: ', datetime.datetime.now() - start)

def show_pow_of_2(max_pow_number=10):
    ''' '''
    
    for i in range(max_pow_number):
        a = int(math.pow(2, i))
        print "2^", i, " - ", a, bin(a)
        print "2^", i, " - ", a-1, bin(a-1)


if __name__ == "__main__":
    random.seed(time.time())
    # random.seed(datetime.now())
    
    # run_benchmark(1000)
    show_pow_of_2()
    


