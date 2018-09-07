#!/usr/bin/python
# ============================================================
#
# ============================================================
import os
import urllib2

class get_prtscr():
    def __init__(self):
        '''Import psutil here due to probable non-existance of this lib in the target device.'''
        self.is_any_process_exist = False
        self.is_psutil_exists = True
        

        try:
            import psutil
            self._psutil = psutil
        except ImportError:
            print "ATTN: Lib 'psutil' is not installed on this computer!"
            self.is_psutil_exists = False

        self.array_to_terminate = []
        self.array_all_process = []
        self.collect_all_runnung_process()

    def set_genie_process_list(self):
        GasModGenie = "GasModGenie.exe"
        GasModTester = "GasModTester.exe"
        AlarmManager = "AlarmManagerGenie.exe"
        GUI = "Genie.exe"
        GUID = "Genied.exe"
        PKPD = "PKPDModeler.exe"
        self.array_to_terminate.append(GUI)
        self.array_to_terminate.append(GUID)
        self.array_to_terminate.append(GasModTester)
        self.array_to_terminate.append(AlarmManager)
        self.array_to_terminate.append(GasModGenie)
        self.array_to_terminate.append(PKPD)

    def set_list_to_terminate(self, _array):
        self.array_to_terminate = _array
    #endif
    
    def get_print(self):
        # os.system("taskkill /im Genied.exe /f")
        self.main_str = "'C:\Program Files (x86)'\IrfanView\i_view32.exe /capture=0 /convert=1.jpg"
        print "\nGet Print screen..."
        os.system(self.main_str)
    #endif

    def kill_process(self, _process_to_kill):
        # os.system("taskkill /im Genied.exe /f")
        print "\nProcess " + _process_to_kill + " will be terminated!"
        exec_line =  "taskkill /im " + _process_to_kill +" /f"
        os.system(exec_line)
    #endif

    def kill_all_processes(self):
        ''' kills all processes from the internal array. If they are exist.'''
        if self.is_psutil_exists:
            self.routine_psutil()
        else:
            self.routine_no_psutil()
    #endif

    def routine_psutil(self):
        ''' kills all processes from the internal array.'''
        for next_genie_proc in self.array_to_terminate:
            if next_genie_proc in self.array_all_process:
                self.kill_process(next_genie_proc)
                self.is_any_process_exist = True
            #end if 
        #endfor
    #endif

    def routine_no_psutil(self):
        ''' kills all processes from the internal array.'''
        for next_genie_proc in self.array_to_terminate:
            self.kill_process(next_genie_proc)
            self.is_any_process_exist = True
        #endfor
    #endif

    def collect_all_runnung_process(self):
        ''' Collect all existing processes by name to an array'''
        if not self.is_psutil_exists:
            return
        #endif

        for p in self._psutil.process_iter():
            self.array_all_process.append(p.name)
            # print p.name
        #end for    
    #endif

    def kill_all_genie_processes(self):
        self.set_genie_process_list()
        self.kill_all_processes()

        if not self.is_any_process_exist:
            print "\n - No Genie processes were found in memory."
    #endif

# main entrance point:
if __name__ == "__main__":

    pk = get_prtscr()
    pk.get_print()
