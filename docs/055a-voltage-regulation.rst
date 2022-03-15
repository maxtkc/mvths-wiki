Voltage Regulation
==========

Overview
--------

Almost all integrated circuits are designed to work within a narrow voltage range. Logic circuits (like microcontrollers) typically work at either 5.0V, 3.3V or 1.8V. Almost all of the circuits you will create in this class will run on either 5.0V or 3.3V. So far, your voltage regulation has come from the USB port on your computer, which provides a voltage of exactly 5 volts, but if you to drive your circuit from a battery you will need some sort of voltage regulation.

Broadly there are two types of voltage regulator ICs, linear and switching. Linear ICs are generally, lower cost, less electrically noisy and provide more current. The downside is that they are less efficient than switching regulators wasting a lot of power. Below is a description of how to regulate voltage using ICs.

The **LM7805** is a common linear regulator for producing 5 volts for your circuit. It is capable of driving 1A of current (almost five times that of the USB port). The LM7805 is also capable of converting input voltages from 6V to 12V to an regulated output of 5V

.. figure:: images/image25.png
   :alt: 

Exercise:
~~~~~~~~~

#. Using the device diagram and the basic circuit shown below, set up an LM7805 to regulate 7V input from your bench supply to 5V output. Test your output using a multimeter. NOTE: your circuit may not produce exactly 5.0V.

   .. figure:: images/image9.png

   .. figure:: images/image16.png

   TEACHER CHECK \_\_\_\_

#. Set up a circuit using the **LD33V**, a 3.3V linear regulator to regulate an input voltage of 8.0V to 3.3V. You will need to look up the datasheet for the LD33V in order to design the circuit.  IMPORTANT! The LD33V does NOT have the samepinout as the LM7805.
