STEP THREE: Using A Breadboard Arduino
==========================

Overview
--------

There are a few differences between using a breadboard-based Arduino versus a Metromini or Arduino Uno. One is that the ATMega328 does not have the pin names conveniently labeled on the IC. The second is that it cannot be directly powered without by a USB cable. Both issues are addressed below.

**Pin Names**: The Metromini and Arduino Uno both have labels to indicate which pins are assigned to digital 0  through digital 13 and analog 0 through analog 5. In order to use these pins correctly with the ATMega328 microcontroller on a breadboard, you will need to learn which of the “Arduino specific” pins are assigned to the actual pins on the microcontroller. 

.. figure:: images/ATmega328-Pinout.png
