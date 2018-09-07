@ECHO OFF
call TDiff.exe
python.exe run.py
call TDiff.exe
beep
