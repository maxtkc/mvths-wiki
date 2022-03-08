Voltage Regulation
==========

Overview
--------

Almost all integrated circuits are designed to work within a narrow voltage range. Logic circuits (like microcontrollers) typically work at either 5.0V, 3.3V or 1.8V. Almost all of the circuits you will create in this class will run on either 5.0V or 3.3V. Circuits are typically powered from either a wall socket or a battery which generally provide voltages above the voltage required for your circuits. For this reason, almost every circuit you design will need some sort of voltage regulation. So far your voltage regulation has come from the USB port on your computer, which provides a voltage of exactly 5 volts but this supply is limited to about 200mA. Below is a description of how to regulate voltage using ICs.

Broadly there are two types of voltage regulator ICs, linear and switching. Linear ICs are generally, lower cost, less noisy. 



Exercise:
~~~~~~~~~

**Linear regulators**
Linear regulators are low cost and easy to use voltage regulators. The downside is that they are not very efficient wasting a lot of power.

LM7805
------

The LM7805 is a common regulator for producing 5 volts for your circuit. It is cable of driving 1A of current (almost five times that of the USB port). The LM7805 is capable of converting input voltages from 6V to 12V to an regulated output of 5V

.. figure:: images/image25.png
   :alt: 

Exercise:
~~~~~~~~~

Using the device diagram and the basic circuit shown below, set up an LM7805 to regulate 10V input from your bench supply to 5V output. NOTE: You will not need to use the capacitors shown for this exercise. Test your output using a multimeter. NOTE: your circuit may not produce exactly 5.0V.

.. figure:: images/image9.png
   :alt: 

Device Diagram

.. figure:: images/image16.png
   :alt: 

Basic Circuit

TEACHER CHECK \_\_\_\_

LD33V
-----

The LD33V is a linear regulator that has a fixed output of 3.3V.

Exercise:
~~~~~~~~~

Set up a circuit using the LD33V to regulate and input voltage of 8.0V to 3.3V. You will need to look up the datasheet for the LD33V in order
to design the circuit.  IMPORTANT! The LD33V does NOT have the same
pinout as the LM7805.
