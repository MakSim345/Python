#!/usr/bin/python
# ============================================================
#
# Copyright (c) 2012 GENERAL ELECTRIC COMPANY
#
# ============================================================
#
# Project:        Intrinsic Carestation SW
#
# Author:         YS / Genie SW Team
#
# ============================================================
# Description: Manage new and old files: compare, rename, etc.
# ============================================================
import os
import hashlib
import zlib

# globals
FILE_BLOCK_SIZE    = 512

class file_manager():
    def __init__(self, _new_file_name = "", _old_file_name = ""):
        '''init '''
        self.set_new_file_name(_new_file_name)
        self.set_installer_file_name(_old_file_name)
        self.uninstaller_file_name = "UninstallGenie.msi"
    #end def
    
    def run(self):
        '''main routine for Genie installer '''
        if os.path.exists(self.installer_file_name):
            self.manage_two_files()
        else:
            # old installer does not exist, so just rename _tmp_file:
            self.rename_tmp_to_target()
            print "\n"
            print "File " + self.installer_file_name + " is ready for installation."
    #end def

    def manage_two_files(self):
        '''Two-steps routine for Genie installation files.'''
        # Compare files md5:
        if self.is_hash_same(self.installer_file_name, self.new_file_name):
            # files are equal, nothig has to be done, except remove new file:
            self.remove_file(self.new_file_name)
            print "File " + self.installer_file_name + " has same MD5 hash as in the SERVER, no need for installation!"
        else:
            # files are different, so action:
            # 1. rename old file to Uninstaller
            self.remove_file(self.uninstaller_file_name)
            self.rename_file(self.installer_file_name, self.uninstaller_file_name)
            # 2. rename tmp file to Installer:
            self.rename_tmp_to_target()
            print "File " + self.installer_file_name + " was updated and ready for installation."
        #end if 
    #end def

    def rename_tmp_to_target(self):        
        '''Rename tmp file to installer_name:'''
        self.rename_file(self.new_file_name, self.installer_file_name)
    #end def

    def set_new_file_name(self, _target_file):
        if (_target_file):
            self.new_file_name = _target_file
    #end def
    
    def set_installer_file_name(self, _target_file):
        if (_target_file):
            self.installer_file_name = _target_file
    #end def
    
    def remove_file(self, _file_to_remove):
        ''' Remove the file '''
        if os.path.exists(_file_to_remove):
            os.remove(_file_to_remove)
            print "File " + _file_to_remove + " deleted succesfully! - OK\n"
    #end def
    
    def rename_file(self, _file_to_rename, _new_name):
        ''' Rename the file '''
        if os.path.exists(_file_to_rename):
            os.rename(_file_to_rename, _new_name)
            # print "File " + _file_to_rename + " renamed succesfully to " + _new_name + "! \n"
    #end def

    def is_hash_same(self, _old_file, _new_file):
        ''' Rename old file '''
        if not os.path.exists(_new_file):                    
            print "ERROR: File " + _new_file + " does not exists!"
            return -1

        if not os.path.exists(_old_file):
            print "ERROR: File " + _new_file + " does not exists!"
            return -1
        
        #os.remove(self.target_file_name)
        
        _md5_hash = md5_hash()
        new_file_md5sum = _md5_hash.get_md5sum(_new_file)
        old_file_md5sum = _md5_hash.get_md5sum(_old_file) 
        
        print "\n"
        print "Local file md5  = " + old_file_md5sum
        print "Remote file md5 = " + new_file_md5sum
        
        if new_file_md5sum == old_file_md5sum:
            print "MD5 sums match!"
            print " "
            return True
        else:
            print "MD5 sums DO NOT match!"
            print " "
            return False        
    #end def

class CRC32(object):
    name = 'crc32'
    digest_size = 4

    def __init__(self, arg=''):
        self.__hash = 0
        self.update(arg)

    def copy(self):
        return self

    def digest(self):
        return self.__hash & 0xffffffff

    def hexdigest(self):
        return '%08x' % (self.digest())

    def update(self, arg):
        self.__hash = zlib.crc32(arg, self.__hash)

# Now you can define hashlib.crc32 = CRC32


class md5_hash():
    def __init__(self):
        '''init '''
        
    def get_bytes(self, file):
        return int(os.stat(file)[6])
    #end def
    
    def get_blocks(self, bytes, block_size):
        return bytes / block_size
    #end def
 
    def get_md5sum(self, _file_to_hash):
        block_size=FILE_BLOCK_SIZE
        
        iso_bytes = self.get_bytes(_file_to_hash)
        blocks  = self.get_blocks(iso_bytes, FILE_BLOCK_SIZE)

        hash = hashlib.md5()
        _file_to_hash = open(_file_to_hash, 'r')
        current_block = 1
        while current_block <= blocks:
            try:
                hash.update(_file_to_hash.read(block_size))
                _file_to_hash.seek(block_size * current_block)
            except IOError:
                # If we get here, it means we dont have the expected number of bytes. 
                #Return the current digest as this should reflect the inconsistant data anyways.
                _file_to_hash.close()
                return hash.hexdigest()
            current_block += 1

        _file_to_hash.close()
        return hash.hexdigest()
    #end def
