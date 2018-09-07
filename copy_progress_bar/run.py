#!/usr/bin/python

# ============================================================
#
#
# ============================================================
#
#
# ============================================================
# ============================================================

import os, sys
import urllib2
import time
import zlib

class logEngine(): 
    
    def __init__(self):
        self._log_file_name = 'dublicate_search.log'

    def saveToLog(self, _text):        
        file = open(self._log_file_name, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("TRACE:\n")
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()

def open_file_safe(_file_name):
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as (errno, strerror):
        print "\nI/O error({0}): {1}".format(errno, strerror)
    except ValueError:
        print "\nCould not convert data to an integer."
    except:
        print "\nUnexpected error:", sys.exc_info()[0]
        raise

def copy_with_pb(SOURCE_FILENAME, TARGET_FILENAME):
    
    print "file to copy " + SOURCE_FILENAME
    TARGET_FILENAME = TARGET_FILENAME+SOURCE_FILENAME
    print "target: " + TARGET_FILENAME
    
    source_size = os.stat(SOURCE_FILENAME).st_size
    print "file to copy " + SOURCE_FILENAME + " has size " + str(source_size)
    
    copied = 0
    source = open(SOURCE_FILENAME, 'rb')
    target = open(TARGET_FILENAME, 'wb')
    _counter = 0
    while True:
        chunk = source.read(32768)
        _counter = _counter + 1
        # print "counter:" , _counter
        if not chunk:
            break
        #end if
        target.write(chunk)
        copied += len(chunk)
        # print '\r%02d%%' % (copied * 100 / source_size),
        if _counter != 0:
            # print '\r%02d%%' % (copied * 100 / source_size),
            _counter = 0
            status = r"%10d  [%3.2f%%]" % (copied, copied * 100. / source_size)
            status = status + chr(8)*(len(status)+1)
            # status = status + '='*(len(status)+1)
            print status,
    #end while

    source.close()
    target.close()
#end def

# main entrance point:
if __name__ == "__main__":
    print ""
    print "app name ", sys.argv[0]
    _str =  sys.argv[1]
    print _str    
    start = time.clock()
    _str =  sys.argv[2]
    print _str 
    SOURCE_FILENAME = "test.avi"
    # size = os.path.getsize("D:/test.avi")
    # print "file to copy " + SOURCE_FILENAME + " has size " + str(size)
    copy_with_pb(sys.argv[1] ,sys.argv[2])
     
    elapsed = (time.clock() - start)
    print "Time taken: " + str(elapsed) + " seconds."
    
    # allperm(str(_str))   
    print ""
    print "Main program end."

