STEP FIVE: Single Supply
===============

Overview
--------

Ultimately, your robot is going to need to be battery powered, so that it is not connected to the USB port and the power supply. In this lesson, you are going to convert your circuit from using two power supplies, one for logic and one for motor power, into a circuit that is powered only by a single supply. It was noted in an earlier lesson that supplying Metro Mini with a voltage higher than 5V would damage the circuit. This is true for all of the pins except one. On the Metro Mini there is a pin labeled Vin. This pin can accept voltages up to 12V because it is connected to an internal voltage regulator that converts the higher voltages to 5v.

Set Up
~~~~~~~~~
#. Write a program that controls your motors in some fashion.
#. Unplug your Metro Mini from the USB port.
#. Confirm that your power supply is still set to 8 volts.
#. Turn off your power supply, but leave the connections from the power supply to the board intact. 
#. Use a long jump wire to connect the VIN on your MD17A to the Vin on your Metro Mini.
#. Ask a teacher to check your circuit.
#. Turn on the power supply. The program you downloaded should now be running.


