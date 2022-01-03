@echo off
TITLE DemonsRobot
:: Enables virtual env mode and then starts aries
env\scripts\activate.bat && python3 -m aries
