#!/usr/bin/env python
import random
from kth_stat import *

def test_on_range():
    assert kth_stat(range(10), 3) == 2

def test_on_shuffled_range():
    li = list(range(10))
    random.shuffle(li)
    assert kth_stat(li, 2) == 2 # incorrect test
    assert kth_stat(li, 3) == 2 # correct test
