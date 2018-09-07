# example for article http://proft.com.ua/parallelizm-v-python/
import time
import threading
import Queue

def factorial(n):
    n = abs(int(n))

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def processing(thread_num, iq):
    while True:
        n = iq.get()
        f = factorial(n)
        iq.task_done()
        print "%d/%d - %d" % (thread_num, threading.active_count(), n)

num_threads = 4
in_queue = Queue.Queue()

t_start_fill = time.time()

for i in xrange(200, 300):
    in_queue.put(i)

t_start_calc = time.time()

for i in xrange(num_threads):
    worker = threading.Thread(target=processing, args=(i, in_queue))
    worker.setDaemon(True)
    worker.start()

in_queue.join()

t_end = time.time()

print "*"*20
print t_end - t_start_fill
print t_end - t_start_calc

