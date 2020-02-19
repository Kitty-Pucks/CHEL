# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:17:46 2020

@author: liamd

This code will get to the 2-on-1 scenario menu

Steps to complete before running code:
    1) Ensure game is in and xbox is plugged in
    2) Resolve internet connection pup up if present (hit "cancel")
    3) Ensure no extra pop-ups will occur (sign in, ea sports account, etc)
    4) Ensure "Practice Mode" is the first pinned gamemode
    5) Get to loading screen of NHL 18 then start
    6) Ensure two on one settings are how you want it (traditional vs competitive, etc)
    
Scenario wanted in step 4:
    1) League = NHL
    2) Team = random
    3) Scenario Type = Rush
    4) Offensive players = 2
    5) Defensive Players = 1
    
    
    Camera angle= zone
"""
import socket
import sys

import RPi.GPIO as GPIO
import time
import random
import cv2

#TODO1: Navigate to Practice Mode game mode
    #Press "A" once to get off loading screen
    #Press "A" to select Practice Mode
    
def prac_mode():
    pin=2
    press(pin)
    time.sleep(20)
    pin=2
    press(pin)
    time.sleep(5)
    
#TODO2: Navigate to "Team Practice"
    #Use D-pad and move to the right three times
    #Press "A" to select team practice
    
def team_prac():
    for i in range(3):
        pin=11
        press(pin)
        time.sleep (1)
    pin=2
    press(pin)
    time.sleep (3)
    
#TODO3: Move to 2-on-1 setup
    
def two_on_one():
    #League=NHL
    pin=10
    press(pin)
    time.sleep(0.5)
    #team = random
    x = random.randint(0,30)    
    print ("team moved left", x, "times")
    for i in range(x):
        pin=10
        press(pin)
        time.sleep(0.5)
    #Scenario = rush
    pin=10
    press(pin)
    time.sleep(0.5)
    #offensive player = 2
    for i in range (2):
        pin=11
        press(pin)
        time.sleep(0.5)
    pin=10
    press(pin)
    time.sleep(0.5)
    #defensive player = 1
    for i in range (2):
        pin=11
        press(pin)
        time.sleep(0.5)
    pin=10
    press(pin)
    time.sleep(0.5)
    pin=2
    press(pin)
    time.sleep(3)
    
#TODO4: Start 2-on-1
def start():
    pin=9
    press(pin)
    time.sleep(0.5)
    pin=2
    press(pin)
    time.sleep(1.5)
    pin=2
    press(pin)
    time.sleep(10)
    
#TODO5: Change sides to no side and set ten minute timer
def side():
    pin=27
    press(pin)
    time.sleep(1)
    for i in range (4):
        pin=10
        press(pin)
        time.sleep(0.5)
    pin=2
    press(pin)
    time.sleep(1)
    pin=10
    press(pin)
    time.sleep(0.5)
    for i in range (2):
        pin=11
        press(pin)
        time.sleep(1)
    pin=3
    press(pin)
    time.sleep(1)
    pin=22
    press(pin)
    time.sleep(0.5)
    pin=2
    press(pin)
    time.sleep(1)
    pin=3
    press(pin)
    time.sleep(0.5)
    pin=2
    press(pin)
    time.sleep(600)
    
#TODO6: End scenario
def end():
    pin=27
    press(pin)
    time.sleep(1)
    for i in range (5):
        pin=10
        press(pin)
        time.sleep(0.5)
    pin=2
    press(pin)
    time.sleep(1)
    pin=22
    press(pin)
    time.sleep(0.5)
    pin=2
    press(pin)
    time.sleep(10)
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


buttons = {"Y": 17,
           "A": 2,
           "B": 3,
           "X": 4,
           "D": 10,
           "U": 22,
           "L": 9,
           "R": 11,
           "Start": 27}


def press (pin):
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.HIGH)
    
#Final
prac_mode()
while True:
    k=cv2.waitKey(1) & 0xFF
    team_prac()
    two_on_one()
    start() 
    side()
    end()
    if k == ord('q'): # press q to end loop
        break
