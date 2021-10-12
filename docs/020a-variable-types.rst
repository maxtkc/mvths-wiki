Variable Types
==============

Overview
--------

So far you have initialized all of your variables as ints.

.. code-block:: c

  int x;
  int counter = 9;

But there are many other numeric variable types supported in C such as ( byte, int, unsigned int, long, unsigned long, float, double. 
Each variable type determines the overall range of numbers the variable supports. For example, an unsigned int supports a range of 0 to 65535. 

.. code-block:: c

  unsigned int r = 5;

This number might seem arbitary but it represents exactly 16 bits. When you initialize an int exactly 16 bits of storage space are reserved for that variable. An 
int, by comparison supports a range of -32768 to +32767. Note that this range represents a total of 65535 possible values (as with an unsigned int) but half of the 
range is positive and half of the range is negative. Essentially, one of the 16 bits is reserved for the sign. A signed int can represent negative numbers as well as 
positive numbers, but an int can represent a higher range of positive numbers.




Potentiometers are another common form of input for controlling an
electronic device. They generally come in two forms: dials and sliders.
Dials are commonly used to control the volume on an audio device or
temperature on a thermostat. Sliders are commonly used in joysticks to
convert the motion of the joystick into signals that can be used by a
digital microcontroller.

Potentiometer Design
--------------------

All potentiometers have three leads as shown in the diagram below. The
two outside leads (A and B) form a fixed value resistor (i.e. the value
