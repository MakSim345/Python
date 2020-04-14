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
        # return the memory usage in percentage
        process = psutil.Process(os.getpid())
        _tmp_mem_load = process.memory_percent()
        # print _tmp_mem_load
        #_tmp_mem_load = psutil.phymem_usage() - deprecated function!
        # mem = '%.0f'%(q.percent/10)
        _mem_load_float = '%.0f'%(_tmp_mem_load*1000)
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
            str_graph = str_graph +  '|'
            #str_graph = str_graph +  chr(254)#'|'
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

def info_loop(max_ctr = 100):
    exit_loop = False
    internal_ctr = 0

    while not exit_loop:
        q = psutil.cpu_percent(interval=1)
        #q = q/10
        cpuload = '%.0f'%(q)
        cpuload = 'cpu load: ' + cpuload + '%'
        print cpuload
        #ser.write(cpuload)
        q = psutil.phymem_usage()
        # mem = '%.0f'%(q.percent/10)
        mem = '%.0f'%(q.percent)
        mem = 'memory: ' + mem + '%'
        print mem
        #ser.write(mem)
        q = psutil.virtmem_usage()
        virtmem = '%.0f'%(q.percent/10)
        virtmem = 'virtmem: '+virtmem  + '%'
        print virtmem
        time.sleep(0.5)
        internal_ctr = internal_ctr + 1
        
        if (internal_ctr > max_ctr):
            self.exit_loop = True 
        print '\n'
        #ser.write(virtmem)
        #ser.close
    #end while
#end def

# main entrance point:
if __name__ == "__main__":
    # print u"Программа началась."
    print ""

    # info_loop(100)
    a = CPU_Info(1000000)
    a.run()

    print ""
    print "Main program end."
