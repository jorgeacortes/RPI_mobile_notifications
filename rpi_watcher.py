#!/usr/bin/python
#GPIO monitoring code. Sends a post to IFTTT Maker when PIN 25 is high.
#Replace <eventname> with your IFTTT event name and <maker-key> with your IFTTT Maker key.
#http://en.jorgeacortes.com/2015/12/getting-mobile-notifications-from-raspberry-pi-gpio/

import os, sys
import RPi.GPIO as GPIO
import time
import requests 
from datetime import datetime

def post(value):
	payload={"value1":str(value),"value2":str(datetime.now())}
	req = requests.post("http://maker.ifttt.com/trigger/<eventname>/with/key/<maker-key>", data=payload)
	print (req.url)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
start=1
past=0
while True:
	now=GPIO.input(25)
	if(now!=past and start==0):
		post(now)
	start=0
	time.sleep(5)
	past=now
GPIO.cleanup()
