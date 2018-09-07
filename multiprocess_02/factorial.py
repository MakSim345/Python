# example for article http://proft.com.ua/parallelizm-v-python/
import time

def factorial(n):
    n = abs(int(n))
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

t_start = time.time()

for i in xrange(200, 300):
    factorial(i)
    #print "%d -> %d" % (i, factorial(i))
    print i

t_end = time.time()

print t_end - t_start
