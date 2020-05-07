https://www.raspberrypi-spy.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/

RPI VIDEO AUDIO

REPAIR SDCARD

“Structure needs cleaning”

sudo umount /dev/sda1

sudo fsck -y /dev/sda1

This second command might need to be run twice. You need to confirm the disk location could be sdc2, etc.

 

# Overview

1.  Follow the above guide for installing an OS, with the only exception you will be installing the version of Raspian with desktop.
2.  Connect RPI to monitor, keyboard, and mouse.
3.  Boot RPI
4.  Add a powered speaker to the audio out port. I have not found that USB speakers work well.
5.  Choose preferences/audio devices and configure your speaker
6.  Navigate to a site that supports sound files and test audio out.
7.  Add a USB camera with microphone.
8.  Test the microphone by running the following:

arecord --device=hw:1,0 --format S16\_LE --rate 44100 -c1 test.wav

This will record signed 16-bit (S16\_LE) audio at 44100 Hz (--rate 44100) mono (-c1) audio to test.wav.

You can have a little VU meter show up if you add to the-V mono command line. Press control-C to quit

9.  Test the wave file by running the command:

aplay test.wav

10. Enable the microphone in Chrome under Settings/Advanced/Content settings
11. Test the video and microphone using either Jitsi or Google Hangouts

EAGLE

# Trace width

Drill: 40

Shape: Long

Diameter: Auto

Trace: 18

1.  Before making a schematic you must power your board by your desired power supply.
2.  All boards must have four mounting holes for 2.5M bolts
3.  All boards must be based on a ATMega328 (not a Metro Mini or Arduino Uno)
