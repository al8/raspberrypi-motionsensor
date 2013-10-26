raspberrypi-motionsensor
========================

from: http://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement/software

prereqs:
  need GPIO
    http://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/necessary-packages
  sudo apt-get update
  sudo apt-get install python-dev
  sudo apt-get install python-rpi.gpio
  sudo apt-get install python-setuptools
  sudo easy_install rpi.gpio

setup:
  RUN these to get motionsensor to run on startup:
  sudo cp initd_motionsensor.sh /etc/init.d/
  sudo update-rc.d initd_motionsensor.sh defaults
  sudo /etc/init.d/initd_motionsensor.sh start
