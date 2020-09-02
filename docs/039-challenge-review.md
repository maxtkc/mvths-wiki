# Challenge Review

## Overview

In this challenge you will construct an LED clock using the DS1307 real time clock and the seven segment display. This will require you to combine the code from each file into one file. A recommendation is to start with the simplest version of one of the two code files and slowly (one line at a time) add code from the other file. You should test the code every time you add a new line. Here are some additional suggestions:

  - use the necessary headers (.h files) for both devices
  - define a variable (object) for each device.
  - set the time
  - begin both the clock and the display
  - get the time in the loop
  - print values to the LED using the DEC argument

In order to most easily print the hours and minutes to the LED display, you can combine the two using the following equation. Note that multiplying the hour by 100 you are shifting it two places to the right on the display.

####   int value = clock.hour \* 100 + clock.minute;

This is a VERY challenging challenge\!

TEACHER CHECK \_\_\_\_
