#!/usr/bin/env python

import time
import RPi.GPIO as io
io.setmode(io.BCM)
 
pir_pin = 23
 
io.setup(pir_pin, io.IN)         # activate input
 
while True:
    if io.input(pir_pin):
        print("PIR ALARM! %d" % time.time())
    time.sleep(0.5)

