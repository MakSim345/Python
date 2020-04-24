If serial port is accesable only by root:
    ("Permission denied on /dev/ttyACM0")
    1. 
    To solve the problem, I had to remove the modemmanager via:
    > sudo apt remove modemmanager
    After a reboot, minicom (and putty) works without root!
    Of course, you also need to be in the dialout group:
    > sudo adduser $USER dialout
    
    2. > sudo chmod a+rw /dev/ttyACM0

