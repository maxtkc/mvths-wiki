Buttons
=======

Overview
--------

Buttons represent the most common form of input found on electronic
devices and are used for everything from turning on the device to
controlling the sound level on your phone. All buttons have exactly
two states. The button is either pressed or it is not pressed. There are
no states in between. For this reason they can be categorized as binary
devices.

.. figure:: images/image70.png
   :alt: 

Button Circuit
--------------

In order to make the states of the button readable by a digital
electronic device such as your microcontroller, you will need to
construct a circuit that converts the states of pressed and not pressed
into voltage levels that the microcontroller can use.

.. figure:: images/image50.png
   :alt: 

Above are two examples of the same circuit. On the left the switch is
open and on the right the switch is closed. When the switch is open, the
circuit produces a voltage level of 0 Volts or LOW as represented in your code. When the switch is closed, the circuit
produces 5 Volts or HIGH as represented in your code. 

The value of 0 Volts or 5 Volts is measured at the line of the diagram labled "input" or where the wire connects the button to the microcontroller.
Note that voltage is always measured as a potential between two points. Most often one point is ground. In this case, the voltage is 
meausred between "input" and ground.

Note that in diagram on the right (labeled closed switch) even though the input is also tied to GND through a
resistor, the voltage is pulled almost completely to 5 Volts.

Exercise
~~~~~~~~

Construct the circuit shown below on your breadboard. Using a `multimeter <https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.j0omxa6kuin>`__
measure the input voltage (between Point A and ground) for the circuit with the button pressed and
not pressed. Make sure to include your units. Complete the following table in your notebook.

.. figure:: images/image15.png
   :alt: 

+---------------+--------------------------+
|               | Output Voltage Point A   |
+---------------+--------------------------+
| Pressed       |                          |
+---------------+--------------------------+
| Not Pressed   |                          |
+---------------+--------------------------+

TEACHER CHECK \_\_\_\_

Exercise:
~~~~~~~~~

Construct a circuit that uses a button to turn on an LED. Unlike in previous circuits, the button should not be directly connected to the LED circuit. 
The button should be connected to your microcontroller as shown above. Connect an LED to a separate pin on your microcontroller. Write a program to read the 
value of the button press (either HIGH or LOW). When the button is pressed, the LED should turn on. If you need help with this exercise, review the lesson `Input Pins <https://mvths-wiki.readthedocs.io/en/latest/012a-input-pins.html#>`__.




TEACHER CHECK \_\_\_\_
