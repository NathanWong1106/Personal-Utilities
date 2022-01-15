:: Given the name of a file in the current directory compiles and runs with gcc
:: !PREREQ!: must have gcc added to PATH

:: I have zero experience writing batch scripts. 
:: I assume that this script is absolutely horrific as a result and apologize in advance.
@echo off

set /P fileName=Enter file name (do not include file extension ".c"): 
set cFileExtension=.c

set cFile=%fileName%%cFileExtension%

echo Attempting to compile %cFile% using gcc
gcc %cFile% -o %fileName%

if %errorlevel% == 0 (


echo Attempting to run .exe
echo ------------------------OUTPUT----------------------------
echo:

%fileName%.exe

echo:
echo -------------------------END------------------------------
echo Finished running

exit
)

echo:
echo COMPRUNC: An error occured during compilation. Stopping execution.
