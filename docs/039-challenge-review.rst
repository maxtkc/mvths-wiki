Challenge Review
================

Overview
--------

This is a VERY challenging challenge! In this challenge you will construct an LED clock using the DS1307 real time clock and the seven segment display. This will require you tocombine the code from each file into one file. A recommendation is to start with the simplest version of one of the two code files and slowly (one line at a time) add code from the other file. You should test the code every time you add a new line. Here are some additional suggestions:

-  use the necessary headers (.h files) for both devices
-  define a variable (object) for each device.
-  set the time
-  begin both the clock and the display
-  get the time in the loop
-  print values to the LED using the DEC argument

In order to most easily print the hours and minutes to the LED display, you can use the following equation. Note that multiplying the hour by 100 you are shifting it two places to the right on the display.

.. code-block:: C

  int value = clock.hour \* 100 + clock.minute;



TEACHER CHECK \_\_\_\_
