#!/usr/bin/python

# ============================================================
#
#
# ============================================================
#
#
# ============================================================
# Description: get a Genie installation file from remote site.
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
        if not chunk:
            break
        #end if
        target.write(chunk)
        copied += len(chunk)
        if _counter == 0:
            #print '\r%02d%%' % (copied * 100 / source_size),
            _counter = 0
            status = r"%10d  [%3.2f%%]" % (copied, copied * 100. / source_size)
            status = status + chr(8)*(len(status)+1)
            print status,
    #end while

    source.close()
    target.close()
#end def

def form_dict():
    my_dict = {}    
    for i in range(0, 127):
        my_dict[i] = chr(i)
    #end for
    # print my_dict
    return my_dict
#end def

def encode_val(word):
    list_code = []
    lent = len(word)
    my_dict = form_dict() 
    for w in range(lent):
        for value in my_dict:
            # if word[w] == my_dict[value]:
            if word[w] == my_dict[value]:
               list_code.append(value) 
            #end if
        #end for
    #end for 
    # short notation:
    #my_dict = form_dict()
    #return [k for c in word for k,v in my_dict.items() if v == c]
    return list_code
#end def

def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict() 

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code
#end def

def comparator(value, key):
    len_key = len(key)
    ret_dictionary = {}
    iter = full = 0
    for i in value:
        ret_dictionary[full] = [i, key[iter]]
        print ret_dictionary
        full = full + 1
        iter = iter + 1
        
        if (iter >= len_key):
            #reset key
            iter = 0 
        #endif

    return ret_dictionary
#end def

def full_encode(value, key):
    dic = comparator(value, key)    
    print 'Compare full encode', dic    
    lis = []
    d = form_dict()
    print "len(dic) = " , len(d)
    for v in dic:
        go = (dic[v][0] + dic[v][1]) % len(d)
        lis.append(go) 
        print lis
    return lis
#end def

def test():
    decoded = full_decode(shifre, key_encoded)
    print 'Decode list=', decoded
    decode_word_list = decode_val(decoded)
    print 'Word=',''.join(decode_word_list)
    

# main entrance point:
if __name__ == "__main__":
    print ""
    start = time.clock()
    
    word = 'crypto'
    key  = 'key'
    
    print 'Word: '+ word
    print 'Key: '+ key

    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
 
    print 'Value= ',value_encoded
    print 'Key= ', key_encoded
    
    shifre = full_encode(value_encoded, key_encoded)
    print 'Code=', ''.join(decode_val(shifre))
    
    elapsed = (time.clock() - start)
    print "Time taken: " + str(elapsed) + " seconds."    
    print "Main program end."

