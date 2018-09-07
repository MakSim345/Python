import multiprocessing
import math

cpu_count = 3

print list(multiprocessing.Pool(processes = cpu_count).map(math.exp,range(1, 2)))


