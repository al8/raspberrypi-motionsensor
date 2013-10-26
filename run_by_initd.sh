#!/bin/bash
echo 0 > /tmp/motionsensor.value
chown -R pi /tmp/motionsensor.value
chgrp -R pi /tmp/motionsensor.value
chmod 666 /tmp/motionsensor.value
((/home/pi/raspberrypi-motionsensor/motionsensor.py -o /tmp/motionsensor.value 2>&1) & echo $! >&3) 3> $1 &
