#!/usr/bin/python


#############################################################################################
#############################################################################################
#
#   The MIT License (MIT)
#   
#   Copyright (c) 2016 http://odelay.io 
#   
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#   
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#   
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
#   
#   Contact : <everett@odelay.io>
#  
#   Description : Simple Mapping of GPIO to Relay block using Node-Red UI
#
#   Version History:
#   
#       Date        Description
#     -----------   -----------------------------------------------------------------------
#      20OCT2016     Original Creation
#
#############################################################################################
#############################################################################################

import RPi.GPIO as GPIO
import time
import sys
import datetime
import time

#-----------------------------------------------
# Grab parameters from Node-Red 
#-----------------------------------------------
duration = int(sys.argv[1])
area = sys.argv[2]


#-----------------------------------------------
# Setup the GPIO on RPi
#-----------------------------------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

#-----------------------------------------------
# Mapping Node-Red Area to GPIO Pin
#-----------------------------------------------
# Area 1 is mapped to GPIO 21 == Pin 40
if(area == 'area1'):
  pin = 40;
# Area 2 is mapped to GPIO 20 == Pin 38
elif(area == 'area2'):
  pin = 38;
# Area 3 is mapped to GPIO 16 == Pin 36
elif(area == 'area3'):
  pin = 36;
# Area 4 is mapped to GPIO 12 == Pin 32
elif(area == 'area4'):
  pin = 32;
else:
  pin = -1;


#-----------------------------------------------
# Drive the GPIO for the configured duration
#-----------------------------------------------
if(pin == -1):
  print "ERROR: Area " + str(area) + " does not exist";
else:
  GPIO.output(pin, GPIO.HIGH)
  for i in range(1,duration+1):
    print "Time Remaining " + str(duration-i) + " sec"
    time.sleep(1)
  
  GPIO.output(pin, GPIO.LOW)

  # Return time stamp
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  print "Last Run Time : " + st

