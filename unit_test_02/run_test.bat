@echo off
@echo .........................................................................
@echo

REM
REM
REM

set PYTHON_TEST_RUN=python -m unittest
set MODULE_TO_TEST=test_circle

:INIT

REM call python -m unittest test_circle
call %PYTHON_TEST_RUN% %MODULE_TO_TEST%

goto SUCCESS

:FAIL
@echo Error occures!
goto END

:SUCCESS

goto END

:END

