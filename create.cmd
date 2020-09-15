echo off
cd C:\Users\USERNAME\Documents\Code\
set arg1=%1
set arg2=%2
shift
shift
python Selenium.py %arg1%
mkdir %arg1%
cd %arg1%
git init
git remote add origin https://github.com/USERNAME/%arg1%
git add .
git commit -m "Initial Commit"
git push -u origin master
%arg2% .
