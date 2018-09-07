import urllib2
import os

class process_kill():
    def __init__(self):
        '''- '''
        self.array_to_terminate = []

    def set_genie_process_list(self):
        GasModGenie = "GasModGenie.exe"
        GasModTester = "GasModTester.exe"
        AlarmManager = "AlarmManagerGenie.exe"
        GUI = "Genied.exe"        
        PKPD = "PKPDModeler.exe"        
        self.array_to_terminate.append(GUI)
        self.array_to_terminate.append(GasModTester)
        self.array_to_terminate.append(AlarmManager)
        self.array_to_terminate.append(GasModGenie)
        self.array_to_terminate.append(PKPD)
    
    def set_list_to_terminate(self, _array):
        self.array_to_terminate = _array
    #endif    

    def kill_process(self, _process_to_kill):
        # os.system("taskkill /im Genied.exe /f")
        print "\nProcess " + _process_to_kill + " will be terminated!" 
        exec_line =  "taskkill /im " + _process_to_kill +" /f"
        os.system(exec_line)
    #endif    

    def kill_all_processes(self):
        ''' kills all processes from the internal array'''
        for key in self.array_to_terminate:
            # print key
            self.kill_process(key)
        #end_for
    #endif

    def kill_all_genie_processes(self):
        self.set_genie_process_list()
        self.kill_all_processes()
    #endif



# main entrance point:
if __name__ == "__main__":    

    print "Main program begins"
    print ""
    
    pk = process_kill()
    pk.kill_process("Skype.exe")
    # pk.kill_process("Mobile Partner.exe")
    # pk.kill_all_genie_processes()
        
    print ""    
    print "Main program ends"
