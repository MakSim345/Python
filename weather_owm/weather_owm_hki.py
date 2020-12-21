#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyowm
import string
import os
import time
import sys, traceback
from datetime import date
from owm_auth import user_token

u_token = user_token()
MY_KEY = u_token.token

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    owm = pyowm.OWM(MY_KEY)
    # hki = owm.three_hours_forecast('Helsinki, FI')
    # print(hki.will_have_clouds())
    # print hki
    hki = owm.weather_at_place('Helsinki, FI')
    weather = hki.get_weather()
    hki_temperature = weather.get_temperature('celsius')['temp']
    print "Helsinki current temperature:", hki_temperature, "*C"

    hki_temperature = weather.get_temperature('celsius')['temp_min']
    print "Helsinki MIN temperature:", hki_temperature, "*C"

    # la = owm.three_hours_forecast('Los Angeles, US')
    # print(la.will_have_clouds())

    print ""
    print "Main program end."
