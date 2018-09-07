# -*- coding: utf-8 -*-
import threading, Queue, time
import traceback

class Worker(threading.Thread):
    def __init__(self, queue, _id_number = 0):
        threading.Thread.__init__(self)
        self.__queue = queue
        self.kill_received = False # флаг прекращения работы
        self._id = _id_number

    def run(self):
        while not self.kill_received:

            try:
                item = self.__queue.get_nowait() # ждём данные
            except Queue.Empty:
                break

            try:
                self.work(item)
            except Exception:
                traceback.print_exc()

            time.sleep(0.5)
            self.__queue.task_done() # задача завершена
            self.__queue.put(item) # зациклим
        #end while

        return

    def work(self, item):
        print "thead number ", self._id, item

def main():
    queue = Queue.Queue()
    num_threads = 5 # 5 потоков

    threads = []
    for x in xrange(100):
        queue.put(x) # заносим данные в очередь
    #end for

    for i in xrange(num_threads):
        t = Worker(queue, i) # создаем нить
        threads.append(t)
        t.start() # стартуем
        time.sleep(0.1)
    #end for

    #Пока в "живых" не останется только главный поток, ждем.
    while threading.activeCount() > 1:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print "Ctrl-c received! Sending kill to threads..."
            for t in threads:
                t.kill_received = True # даем сигнал о завершении всем потокам
            #end for
    #end while

    print "Done!"


if __name__ == '__main__':
    main()

