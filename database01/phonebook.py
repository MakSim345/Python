#!/usr/bin/env python

#############################################################################
## 2011 YS
##
#############################################################################

import sqlite3
import math
import os, sys
import traceback

class Data_Base_Core():
    def __init__(self,  args = sys.argv[1:]):
        self._exit = False
        self.string_db_name = 'test_phonebook.db'
        # self.con

    def connect_data_base(self, str_db_name):
        self.con = sqlite3.connect(str_db_name)
        self.cur = self.con.cursor()

    def create_table(self):
        # Create Item table
        self.cur.execute('CREATE TABLE phonebook01 (o_id INTEGER PRIMARY KEY, name STRING, phone STRING)')
        self.con.commit()

    def insert_into_table(self, str_to_insert = ""):
        #self.cur.execute('INSERT INTO foo (o_id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
        #self.cur.execute('INSERT INTO phonebook01 VALUES(NULL, "Yuriy", "0675589855")')
        #self.cur.execute('INSERT INTO phonebook01 VALUES(NULL, "Anna",  "0404533658")')
        self.cur.execute(str_to_insert)

        self.con.commit()
        print self.cur.lastrowid

    def get_table(self, str_to_exec):
        self.cur.execute(str_to_exec)
        return self.cur.fetchall()

    def showSubItem(self, subPart):
        subPart = '"%' + subPart + '%"'
        string_to_execute = 'SELECT * FROM phonebook01 WHERE phone LIKE ' + subPart  #"%33%"'
        print string_to_execute
        self.db_result = self.get_table(string_to_execute)
        self.printResult()

    def showAll(self):
        string_to_execute = 'SELECT * FROM phonebook01'
        self.db_result = self.get_table(string_to_execute)
        self.printResult()

    def printResult(self):
        print('-'*40)
        for row in self.db_result:
            print row[0], row[1], row[2]
        print('-'*40)
        self.db_result = ""

    def test_database(self):
        # string_to_execute = 'SELECT * FROM foo WHERE fruit="cherry"'
        # string_to_execute = 'SELECT * FROM phonebook01 WHERE name="Marika"'
        string_to_execute = 'SELECT * FROM phonebook01'
        # string_to_execute = 'SELECT * FROM phonebook01 WHERE phone like "%33%"'
        # string_to_execute = 'SELECT * FROM my_table_item'
        # string_to_execute = 'SELECT * FROM my_table_item WHERE price=8.44'
        # string_to_executering_db_name = 'mydatabase.db'
        try:
            # connect_data_base(string_db_name)
            # create_table(cursor_db, connect_db)
            # insert_table(cursor_db, connect_db)
            db_result =  get_table(string_to_execute)
            print('-'*40)
            for row in db_result:
                print row[0], row[1], row[2]
            print('-'*40)
        except:
            print "1. Error occures: unknown"
            traceback.print_exc()

    def addNewItem(self, _input_name, _input_phone):
        str_for_inset = 'INSERT INTO phonebook01 VALUES(NULL, "' + _input_name + '", "' + _input_phone + '")'
        self.insert_into_table(str_for_inset)

    def Exit(self):
        #self.BackUp.exit_thread()
        #self.Main.exit_thread()
        self._exit = True

    def check_user(self, credentials_str):
        try:
            user, passwd = credentials_str.strip().split(":")
            return self.__users_db.check(user, passwd)
        except ValueError:
            return False;
        #try
    #def    

    def main(self):
        print "\n"
        
        #TODO here - prompt password and compare it with one from file md5.

        print "Open DataBase:", self.string_db_name
        self.connect_data_base(self.string_db_name)

        while not self._exit:
            _user_input = raw_input('\nPlease enter your command:\n > ')

            if (_user_input == ":exit") or (_user_input == ":quit") or (_user_input == ":q"):
                self.Exit()
            elif (_user_input == ":m") or (_user_input == ":menu"):
                self.showMenu()
            elif (_user_input == ":l") or (_user_input == ":list"):
                self.showAll()
            elif (_user_input == ":add"):
                _user_input_name = raw_input('Please enter follow information\nName:\n > ')
                _user_input_phone = raw_input('Phone number:\n > ')
                self.addNewItem(_user_input_name, _user_input_phone)
            elif (_user_input == ":f") or (_user_input == ":find"):
                _user_input = raw_input('\nPhone number (or part):\n > ')
                self.showSubItem(_user_input)
            elif (_user_input == ":t") or (_user_input == ":test"):
                _month = int(time.strftime("%m"))
                _date =  time.strftime("%d")+"-"+self._month_str.get(_month)
                _user_input = _date + time.strftime(" %Hh %Mmin %Ssek\n") + "TecTuk - Ha npegMeT npoBepku cBq3u."
            else:
                if len(_user_input):
                    # self.send_sms_in_threads(True, True, _user_input)
                    pass
                else:
                    print "Your message is", len(_user_input), "characters long. It is too short for sending. \nMessage WAS NOT sent."
            #except:
            #    print "Unknown error occures:"
            #    traceback.print_exc()

        # wait for threads to complete:
        #self.writeActiveSessionToConfigFile()
        #self.BackUp.join()
        # raw_input("\n\nPress the enter key to exit.")

class DB_Engine():
    def __init__(self,  args = sys.argv[1:]):
        self._exit = False
        self._config_file_name = "db_settings.ini"
        self._log_file_name = "myfile.txt"
        self.body = " " # empty message!
        self._month_str = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR',
                           5:'MAY', 6:'JUN', 7:'JUL', 8:'AUG',
                           9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
        self.args = args

        self.readConfigFile()
        self.writeConfigFile()
        self.initProvider()
        self.initMainSender()
        self.initBkpSender()
        self.createPoolOfThreads()
        self.setProviderToThreads()
        self.setSenderToThread()
        self.startThreads()

    def writeActiveSessionToConfigFile(self):
        cf = configFile(self._config_file_name)
        cf.setKey("ACTIVE_SESSION", "last_active_name", self._main_name)
        cf.setKey("ACTIVE_SESSION", "last_active_address", self._main_address)
        cf.setKey("ACTIVE_SESSION", "last_active_provider", self._last_active_provider)

    def writeConfigFile(self):
        cf = configFile(self._config_file_name)
        cf.setKey("GENERAL", "TODAY_DATE", time.strftime("%Y-%m-%d %H:%M:%S"))

    def readConfigFile(self):
        cf = configFile(self._config_file_name)

        # If no arguments, we will read last active session info:
        try:
            if not self.args:
                self._main_address = cf.getKey("ACTIVE_SESSION", "last_active_address")
                self._main_name =    cf.getKey("ACTIVE_SESSION", "last_active_name")
            else:
                self._main_address = cf.getKey("ADDRESS", self.args[0])
                self._main_name = self.args[0]

                #print self._main_address
        except:
            print "Error occures in readConfigFile."
            self._main_address = cf.getKey("ACTIVE_SESSION", "last_active_address")
            self._main_name =    cf.getKey("ACTIVE_SESSION", "last_active_name")
            # traceback.print_exc()

        self._bkp_address = cf.getKey("ADDRESS", "yuriy")

        # provider shall always be from the last session?:
        self._last_active_provider = cf.getKey("ACTIVE_SESSION", "last_active_provider")
        self._provider_server = cf.getKey(self._last_active_provider, "provider_server")
        self._from_addr = cf.getKey(self._last_active_provider, "from")
        self._username = cf.getKey(self._last_active_provider, "username")
        self._password = cf.getKey(self._last_active_provider, "password")

    def initProvider(self):
        self._mail_provider = mail_provider()
        self._mail_provider.setServerAddr(self._provider_server)
        self._mail_provider.setUsername(self._username)
        self._mail_provider.setPassword(self._password)

    def initMainSender(self):
        self.sender_main = general_sender()
        self.sender_main.setFrom(self._from_addr)
        self.sender_main.setTo(self._main_address)
        self.sender_main.setNickName(self._main_name)

    def initBkpSender(self):
        self.sender_backup = general_sender()
        self.sender_backup.setFrom(self._from_addr)
        self.sender_backup.setTo(self._bkp_address)
        self.sender_backup.setNickName("BKP")

    def setMessageBody(self, strBody):
        self.body = strBody
        self.sender_main.setMsgBody(self.body)
        self.sender_backup.setMsgBody(self.body)

    def messageBody(self):
        return self.body

    def saveMessageToLog(self):
        file = open(self._log_file_name, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("TO: " + "(" + self.sender_main.nickName + ")" + self.sender_main.toaddrs + "\n")
        file.write("Message: [ " + self.messageBody() + " ]\n")
        file.write("-------------------------------------\n\n")
        file.close()

    def createPoolOfThreads(self):
        self.BackUp = SendingThread()
        self.Main = SendingThread()

    def setProviderToThreads(self):
        self.Main.set_provider(self._mail_provider)
        self.BackUp.set_provider(self._mail_provider)

    def setSenderToThread(self):
        self.BackUp.set_sender(self.sender_backup)
        self.Main.set_sender(self.sender_main)

    def showMenu(self):
        print "Here we will have a menu."
        # here we will change sender, provider, or else...

    def Exit(self):
        self.BackUp.exit_thread()
        self.Main.exit_thread()
        self._exit = True

    def startThreads(self):
        self.Main.start()
        self.BackUp.start()

    def send_sms_in_threads(self, send_to_main = True, send_to_backup = True, str_user_input = 'TECT'):
        self.setMessageBody(str_user_input)
        self.saveMessageToLog()
        if send_to_main:
            self.Main.send_sms()
        if send_to_backup:
            self.BackUp.send_sms()
        print  "OK - Message sent to", self.sender_main.nickName, "-",  self.sender_main.toaddrs

    def main(self):
        print "\n"
        print "Message will be sent to", self.sender_main.nickName, "-",  self.sender_main.toaddrs
        print "Mail provider:", self._last_active_provider
        while not self._exit:
            _user_input = raw_input('\nPlease enter your message:\n > ')

            if (_user_input == ":exit") or (_user_input == ":quit") or (_user_input == ":q"):
                self.Exit()
            elif (_user_input == ":m") or (_user_input == ":menu"):
                self.showMenu()
            elif (_user_input == ":t") or (_user_input == ":test"):
                _month = int(time.strftime("%m"))
                _date =  time.strftime("%d")+"-"+self._month_str.get(_month)
                _user_input = _date + time.strftime(" %Hh %Mmin %Ssek\n") + "TecTuk - Ha npegMeT npoBepku cBq3u."
                print _user_input
                self.send_sms_in_threads(True, True, _user_input)
            else:
                if len(_user_input):
                    self.send_sms_in_threads(True, True, _user_input)
                else:
                    print "Your message is", len(_user_input), "characters long. It is too short for sending. \nMessage WAS NOT sent."
            #except:
            #    print "Unknown error occures:"
            #    traceback.print_exc()

        # wait for threads to complete:
        self.writeActiveSessionToConfigFile()
        self.BackUp.join()
        # raw_input("\n\nPress the enter key to exit.")

if __name__ == '__main__' or __name__ == sys.argv[0]:
    mw = Data_Base_Core(sys.argv[1:])
    sys.exit(mw.main())

