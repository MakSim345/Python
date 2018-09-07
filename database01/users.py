#!/usr/bin/env python

import os
import csv
from hashlib import md5

class users:
    def __init__(self, users_db_path):
        if users_db_path is None:
            raise ValueError("Passed null as users_db")

        self._users = {}
        self._users_db_path = users_db_path
        if os.path.exists(self._users_db_path):
            self._load_db()
        else:
            print "Database is't exists '%s'" % (users_db_path)
    
    def _load_db(self):
        f = open(self._users_db_path, 'rb')
        c_reader = csv.reader(f, delimiter=',')
        for line in c_reader:
            if not self._users.has_key(line[0]):
                self._users[line[0]] = line[1]
        f.close()

    def check(self, user, passwd):
        return self._users.has_key(user) and self._users[user] == md5(passwd).hexdigest()

    def add(self, user, passwd):
        if not self._users.has_key(user):
            self._users[user] = md5(passwd).hexdigest()
            f = open(self._users_db_path, 'wb')
            for key in self._users.keys():
                f.write("%s,%s\n" % (key, self._users[key]))
            f.close()
