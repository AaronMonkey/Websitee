@echo off
set var=%1
set extract=%var:~6,-1%
start "C:\Program Files (x86)\PuTTY\putty.exe" %extract%