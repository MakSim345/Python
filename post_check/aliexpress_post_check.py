import urllib
import time
import smtplib
import os
import urllib2
from sys import argv

class aliexpress_post_check():
    def __init__(self, days_count = 9):
        # self._url = "http://www.posti.fi/henkiloasiakkaat/seuranta/#/lahetys/RS391035169NL?lang=en"
        # self._url = "http://www.posti.fi/henkiloasiakkaat/seuranta/#/lahetys/RS121339287EE?lang=en"
        self._url = "http://www.posti.com/fi/"
        self.body = ''
        #self.log = logEngine()

    def make_check(self):
        msg = ""
        self._url_result = self._url
        print "open " + self._url_result
        f = urllib2.urlopen(self._url_result)
        msg = f.read()
        # msg = urllib2.urlopen(self._url_result, proxies=proxiesa).read()
        # return self.status_from_xml(msg)
        return msg

    def status_from_xml(self, _txt_to_parce):
        i = _txt_to_parce.find("<resultstring>")+14
        j = _txt_to_parce.find("</resultstring>")
        _status = "\nSMS status: " + _txt_to_parce[i:j]
        if _status != 'success':
            i = _txt_to_parce.find("<description>")+13
            j = _txt_to_parce.find("</description>")
            _error = _txt_to_parce[i:j]
            _status = _status + ". " + _error
        return _status

# main entrance point:
if __name__ == "__main__":
    #print "Main program start."
    #print ""
    a = aliexpress_post_check()
    #sender.msg_body(_user_input)
    print a.make_check()

    print "END."
    #print "Main program end."

