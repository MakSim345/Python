#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
#
#
# ============================================================
#
# ============================================================
# ============================================================
import os
import time
import sys
import psutil

from math import *
import serial
SERIAL_PORT = 'COM4'
# SERIAL_SPEED = 38400
SERIAL_SPEED = 115200
# SERIAL_SPEED = 9600

codepage = 'utf-8'
debug = 0
data_file = 't.txt'
# import serial

# ser = serial.Serial(2)   #Change this according to your own COM-port. 
# Remeber that the value you should add is one less than the number of your COM-port.

class CPU_Info():
    def __init__(self, _max_ctr = 10):
        ''' '''
        self.exit_loop = False
        self.set_internal_ctr(_max_ctr)
        self.internal_ctr = 0
        self.cpuload = 0
        self.vmemload = 0
        self.memload = 0

    def set_internal_ctr(self, _max_ctr = 0):
        self.max_ctr = _max_ctr

    def get_cpu_load(self):
        _tmp_cpu_load = psutil.cpu_percent(interval=0.2)
        self.cpuload = '%.0f'%(_tmp_cpu_load)
        # self.cpuload = 'cpu load: ' + self.cpuload + '%'
        return self.cpuload

    def get_mem_load(self):
        _tmp_mem_load = psutil.phymem_usage()
        # mem = '%.0f'%(q.percent/10)
        _mem_load_float = '%.0f'%(_tmp_mem_load.percent)
        # self.memload = 'memory: ' + _tmp_mem_load_float + '%'
        return _mem_load_float
    
    def get_vmem_load(self):
        _tmp_vmem_load = psutil.virtmem_usage()
        # mem = '%.0f'%(q.percent/10)
        _tmp_vmem_load_float = '%.0f'%(_tmp_vmem_load.percent)
        self.memload = 'virt.memory: ' + _tmp_vmem_load_float + '%'
        return self.vmemload

    def print_info(self):
        cpu_load = self.get_cpu_load()
        mem_load = self.get_mem_load()
        # status = "%d - CPU:%s%% MEMORY:%s%%" % (self.internal_ctr, cpu_load, mem_load)
        status = "%d - MEMORY:%s%% CPU:%s%% " % (cpu_load, mem_load, self.internal_ctr)
        status = status + chr(8)*(len(status)+1)
        print status,

    def print_graph(self):
        str_graph = ''
        cpu_load = self.get_cpu_load()
        mem_load = self.get_mem_load()
        # status = "%d - CPU:%s%% MEMORY:%s%%" % (self.internal_ctr, cpu_load, mem_load)
        # status = "CPU:%s%% MEMORY:%s%%" % (cpu_load, mem_load)
        status = "MEMORY:%s%% CPU:%s%%" % (mem_load, cpu_load)
        print status,
        
        if (int(cpu_load)<=0):
            a = 1
        else:    
            a = 100/(100/int(cpu_load))# int(int(cpu_load)/50)
        # print '-', a , '-',

        for i in range(a):
            str_graph = str_graph + '|'
        #    print '|',
        print str_graph,
        #status = status + str_graph + chr(8)*(len(status + str_graph) + 1)
        #print status,
        print ''
        # status = status + chr(8)*(len(status)+1)
        

    def run(self):
        while not self.exit_loop:
            _str_to_print = self.get_cpu_load() + '\n' + self.get_mem_load() + '\n'
            # _str_to_print = self.get_cpu_load() + ' ; ' + self.get_mem_load()            
            # print "%s" % (_str_to_print),
            _str_to_print = _str_to_print + chr(8)*(len(_str_to_print)+1)
            # print _str_to_print
            # self.print_info()
            self.print_graph()
            
            # time.sleep(0.01)
            self.internal_ctr = self.internal_ctr + 1
            
            if (self.internal_ctr > self.max_ctr):
                self.exit_loop = True 
            # print '\n'
            #ser.write(virtmem)
            #ser.close
        #end while

def print_graph(_value_to_show):
    str_graph = ''
    # print "--", _value_to_show
    # print "---", float(_value_to_show)/100
    # print "---", 100/(100/float(_value_to_show))
    # _load = self.get_cpu_load()

    # status = "%d - CPU:%s%% MEMORY:%s%%" % (self.internal_ctr, cpu_load, mem_load)
    # status = "CPU:%s%% MEMORY:%s%%" % (cpu_load, mem_load)
    # status = "MEMORY:%s%% CPU:%s%%" % (mem_load, cpu_load)
      
    if (int(_value_to_show)<=0):
        a = 1
    else:
        # a = 100/(100/float(_value_to_show))# int(int(cpu_load)/50)
        a = float(_value_to_show)/10 # int(int(cpu_load)/50)
    
    for i in range(int(a)):
        str_graph = str_graph + '|'
        #    print '|',
        # print str_graph,
        #status = status + str_graph + chr(8)*(len(status + str_graph) + 1)
        #print status,
        # print ''
        # status = status + chr(8)*(len(status)+1)
    #end_for
    print str_graph,
    print ''
#end_def

def get_data_from_com():
    print "hello"
    ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)
    while (1):    
    # for i in range(0, 400):
        # s = ser.read()
        s = ser.readline().strip()
        # print str(i), " - ", s, "\n"
        if str.isalnum(s):
            # self.drawdata(float(s))
            print_graph(s)
        #endif
    #end_for
#end_def

# main entrance point:
if __name__ == "__main__":
    # print u"Программа началась."
    print ""

    get_data_from_com()
    
    # info_loop(100)
    #a = CPU_Info(1000)
    #a.run()

    print ""
    print "Main program end."
