#!/usr/bin/python
# ============================================================
#
#
# ============================================================
#
# ============================================================
# Description: Download a file from given URL. 
# ============================================================
import os
import urllib2
import sys, traceback

class get_file():
    def __init__(self, _address = ""):
        '''init address string '''
        self.set_address(_address)
        self.url = ""
        self.tmp_file = "_tmp_file"

    def set_address(self, _address):
        self.address = _address
        self.set_file_name(self.address.split('/')[-1])

    def set_file_name(self, _target_file):
        self.target_file_name = _target_file

    def set_tmp_file_name(self, _target_tmp_file):
        self.tmp_file = _target_tmp_file        

    def remove_prev_tmp_file(self):
        ''' Remove old tmp file.'''
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)
            # print "File " + self.tmp_file + " deleted succesfully! - OK\n"
    #end def

    def open_link(self):
        '''Open a file from given address.'''
        try:
            self.url = urllib2.urlopen(self.address)

        except urllib2.HTTPError, e:
            print "ATTN:",  e
            if e.code == 404:
                print "URL <" + self.address + "> does not exist!"
            else:
                raise
            #traceback.print_exc()

        except urllib2.URLError, e:
            print "ATTN: Can not open follow URL :\n" + self.address + "\n"

        except:
            print "ERROR: Unknown error occures. See traceback:\n"
            traceback.print_exc()
    #end def

    def get_file_progress_bar(self):
        ''' Download a file from given address.'''
        self.open_link()

        if (not self.url):
            # Do nothing if link does not exist.
            return False

        # Erase old tmp file in case it exists:
        self.remove_prev_tmp_file()

        self.f = open(self.tmp_file, 'wb')
        meta = self.url.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (self.target_file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = self.url.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            self.f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,

        self.f.close()
        return True
    #end def

    def get_fresh(self):
        ''' Wrapper for getter function'''
        return self.get_file_progress_bar()
    #endif
