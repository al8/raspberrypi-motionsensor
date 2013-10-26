#!/usr/bin/env python

from __future__ import print_function
 
import argparse
import time
import sys

import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)


def pir_read(pir_pin):
    GPIO.setup(pir_pin, GPIO.IN)  # activate input
    return GPIO.input(pir_pin)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='motionsensor')
    parser.add_argument("--pin", type=int, default=23)
    parser.add_argument("--outfile", "-o", type=str, default="/tmp/motionsensor.value")
    parser.add_argument("--debug", action="store_true")
    options = parser.parse_args()

    if options.debug:
        print("using pin %d" % options.pin)

    while True:                                     
        value = pir_read(options.pin)
        if options.debug:
            print("%s: " % time.asctime(), file=sys.stderr, end='')
            print(value)
        with open(options.outfile, "wb") as f:
            f.write("%d" % value)
        time.sleep(0.5)
