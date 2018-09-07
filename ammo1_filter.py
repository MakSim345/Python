#!/usr/bin/python

import sys

start_from = 110

input = sys.argv[1]
interval = int(sys.argv[2])

output = input + ".out"

def is_good_line(index):
    if index <= 10:
        return True
    if (index - start_from) % interval == 0:
        return True
    return False


with open(input) as f_in:
    with open(output, 'w') as f_out:
        for index, line in enumerate(f_in, 1):
            if is_good_line(index):
                print("Copied line {}".format(index))
                f_out.write(line)

