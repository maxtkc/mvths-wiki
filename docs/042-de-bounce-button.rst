De-Bounce Button
================

Overview
--------

Imagine pressing a momentary button like one on a keypad. The time
during which it is pressed seems to be so short as to be irrelevant, yet
microcontrollers process information at an incredibly fast rate, 16
million cycles per second in the case of the Arduino or one cycle every
62.5 nanoseconds. By this measure our fingers are very slow.

Button Pulse
------------

In order to write code to read a button press, you will need to
understand the length of the average button press. If you wire your
button so that it defaults to LOW, when the button is pressed the output
goes HIGH and when it is released the output goes LOW. This results in a
pulse as shown below.

.. figure:: images/image66.png
   :alt: 

Although the length of time a button is pressed may depend on may depend
on many factors such as the device, or the mood or tendency of the user,
it is possible to work out some useful parameters for button press
length using your oscilloscope.

Exercise
~~~~~~~~

Connect the output of a default low button circuit to your oscilloscope.
For the length of the average button press, try to imagine you are using
a gamepad device or your entering time on your microwave oven. Make sure
to include the correct units.

In order to do this easily, you will need to use the trigger on your
scope.  

        Length of shortest button press:         \_\_\_\_\_\_\_\_\_

        Length of average button press:        \_\_\_\_\_\_\_\_\_

2. TEACHER CHECK \_\_\_\_

Button Software
---------------

The following are two basic strategies for using a button to control the
states within your microcontroller.

-  Direct state control, the state of the button equals the state of the
   device. For example, a direct state control of an LED would turn the
   LED when the button is pressed and off when the button is not
   pressed.
-  Toggle state control, the button can transition a device between two
   states. For example in toggle state control of an LED, the LED would
   change its state (on or off) after each button press.

Exercise
~~~~~~~~

1. Construct a circuit and write a program to demonstrate direct control
   using a button and an LED. The LED should remain on as long as the
   button is pressed and turn off when the button is not pressed.

3. TEACHER CHECK \_\_\_\_

2. Using a single button demonstrate toggle control over one LED. There
   are two ways to solve this problem. One is create a new variable to
   store the state of the button press. The second is to toggle the
   state of the LED. You can find information on toggling an LED on
   line.

NOTE: If your circuit is not reliable (i.e. not consistently changing
states), check the guide on timing and button presses.

4. TEACHER CHECK \_\_\_\_
