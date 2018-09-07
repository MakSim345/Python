@ECHO OFF
call TDiff.exe
python run.py
call TDiff.exe
beep
