import os

class text_utils():
    def __init__(self):
        self._url = "http://www.foreca.com/Finland/Helsinki?tenday"

    def replace_chars(self, _msg):
        #_msg = _msg.replace('j', chr(151))
        #_msg = _msg.replace('L', chr(20))
        #_msg = _msg.replace('l', chr(20))
        #_msg = _msg.replace('F', chr(18))
        #_msg = _msg.replace('f', chr(18))
        #_msg = _msg.replace('r', chr(147))
        
        _msg = _msg.replace('h', 'H')
        _msg = _msg.replace('<', '')
    
        _msg = _msg.replace('bbI', 'BbI')
        
        # not needed:
        # _msg = _msg.replace('n', chr(150))
        # _msg = _msg.replace(':', ';')
        return _msg
    
    def translate_condition(self, word_to_translate):
        a =  str(word_to_translate)
        dictionary = {"Clear":"qcHo", "Mostly clear": "B OcH. qcHo", "Partly cloudy":"O6La4Ho",
                    "Partly cloudy and light rain":"MecTaMu O6La4Ho, He6oLbwue ocagku",
                    "Partly cloudy and light snow":"MecTaMu O6La4Ho, He6oLbwoj cHer",
                    "Partly cloudy and snow showers":"MecTaMu O6La4Ho, cHer c go*geM",
                    "Partly cloudy and light wet snow":"MecTaMu O6La4Ho, MokpbIj cHer",
                    "Partly cloudy and wet snow showers":"MecTaMu O6La4Ho, cHer c go*geM",
                    "Partly cloudy and showers":"MecTaMu O6La4Ho, ocagku",
                    "Cloudy and showers":"O6La4Ho, ocagku",
                    "Cloudy and light rain":"O6La4Ho, MeLkuj go*gb",
                    "Cloudy and snow showers":"O6La4Ho, MokpbIj cHer",
                    "Cloudy and light snow":"O6La4Ho, MeLkuj cHer",
                    "Cloudy":"O6La4Ho",  
                    "Overcast":"nacMypHo",
                    "Overcast and showers":"nacMypHo, ocagku",
                    "Overcast and rain":"nacMypHo, go*gu",
                    "Overcast and wet snow":"nacMypHo, MokpbIj cHer",
                    "Overcast and light wet snow":"nacMypHo, He6oLbwoj MokpbIj cHer",
                    "Overcast and snow":"nacMypHo, cHer",
                    "Overcast and wet snow showers":"nacMypHo, MokpbIj cHer c go*geM",
                    "Overcast and snow showers":"nacMypHo, MokpbIj cHer",
                    "Overcast and light rain":"nacMypHo, He6oLbwue ocagku",
                    "Overcast and light snow":"nacMypHo, He6oLbwoj cHer",
                    "Overcast, thunderstorms with rain":"nacMypHo, go*gu u rpo3bI",
                    "Partly cloudy, possible thunderstorms with rain":"O6La4Ho, Bo3M.go*gu u rpo3bI"}
        try:
            return dictionary[a]
        except:
            print "ATTN: no such word in dictionary:", word_to_translate, "!"
            return word_to_translate
    
    def translate_weekday(self, word_to_translate):
        a =  str(word_to_translate)
        dictionary = {"Mon":"nH", "Tue":"BT", "Wed":"Cp", "Thu":"4T", "Fri":"nT", "Sat":"C6", "Sun":"Bc"}
        #dictionary = {"Mon":"nHg", "Tue":"BTp", "Wed":"Cpg", "Thu":"4TB", "Fri":"nTH", "Sat":"C6T", "Sun":"Bck"}
        try:
            return dictionary[a]
        except:
            #print "ATTN: no such word in dictionary:", word_to_translate, "!"
            return word_to_translate

    def translate_month(self, month_to_translate):
        a =  str(month_to_translate)
        dictionary = {"Jan":".01", "Feb":".02", "Mar":".03", "Apr":".04", "May":".05", "Jun":".06", "Jul":".07", "Aug":".08","Sep":".09","Oct":".10","Nov":".11","Dec":".12"}
        #dictionary = {"Mon":"nHg", "Tue":"BTp", "Wed":"Cpg", "Thu":"4TB", "Fri":"nTH", "Sat":"C6T", "Sun":"Bck"}
        try:
            return dictionary[a]
        except:
            print "ATTN: no such word in dictionary:", month_to_translate, "!"
            return month_to_translate
