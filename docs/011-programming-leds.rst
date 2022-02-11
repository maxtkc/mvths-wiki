Programming Leds
================

Overview
--------

LEDs are a good example of the kinds of devices you can drive with a microcontroller. LEDs also provide an easy way to indicate if a microcontroller pin is set to HIGH or LOW. **IMPORTANT:** You **MUST** to a resistor in series with any LED to prevent the LED from burning out. Driving too much current through and LED will damage the LED and potentially the microcontroller.

Exercise:
~~~~~~~~~

#. Follow the schematic below to connect an LED to your microcontroller. 

.. figure:: images/image84.png
  
**IMPORTANT:** Each pin on the microcontroller should only be used as you intend to use it. In the image below, the user is intending to control the LED with pin 5, but has inadvertently connected the other lead of the LED to pin 2.

.. image:: images/ledwrong.JPG
   :width: 400px
   
In the correct example below, the user has used a jump wire to connect the LED, so that only pin 5 is being used.

.. image:: images/ledright.JPG
   :width: 400px



#. 

Write a program to turn on the LED. NOTE: In this lesson you will be
   choosing which digital pin to use with you LED. You may use any of
   the digital pins (0 - 13) but you should generally avoid using digital
   pins 0 and 1 as using these pins might interfere with the programming
   of your device.

.. raw:: html

   <!-- end list -->

2. Set the pin you are using to control the LED as an output pin.
3. Use digitalWrite to drive the pin to 5V.

TEACHER CHECK \_\_\_\_\_

3. Modify your program to turn off the LED.
4. Change the LED to a different pin and turn it on.
5. Add two more LEDs to two additional pins on your microcontroller and
   turn them all on.

TEACHER CHECK \_\_\_\_\_


