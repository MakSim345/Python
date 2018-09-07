#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

# The easiest way is to just interrupt it with the usual Ctrl-C (SIGINT).

try:
    while True:
        do_something()
except KeyboardInterrupt:
    pass
    #end_while

#---------------
import time, sys
x = 1
while True:
  try:
      print x
      time.sleep(.3)
      x += 1
  except KeyboardInterrupt:
      print "Bye"
      sys.exit()
#end_while
#---------------
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        exit_gracefully()


# Since Ctrl-C causes KeyboardInterrupt to be raised, just catch it outside the loop and ignore it.




# There is a solution that requires no non-standard modules and is 100% transportable
import thread

def input_thread(list):
    raw_input()
    list.append(None)

def do_stuff():
    list = []
    thread.start_new_thread(input_thread, (list,))
    while not list:
        stuff()


