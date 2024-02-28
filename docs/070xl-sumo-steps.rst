STEP TWO: Driving One Motor
=============================

Overview
--------
In this lesson, you will be turn a motor on and off and control its direction using logic. 

Set Up
--------
Set up our initial breadboard circuit with a Metro Mini and the motor controller

#. Set up a breadbord with just a Metro Mini and the usual power and ground connections. (DO NOT CONNECT A USB CABLE YET)
#. Add the MD17A to your board.
#. Following the diagram in the previous lesson, connect both GND pins to ground on your breadboard.
#. Connect the two leads of your motor to AOUT2 and AOUT1. It does not matter which lead of the motor goes to which pin.
#. Using long jump wires, connect the AIN1 pin to ground and AIN2 to power. These are you control pins and will be used to turn the motor on and off and control its direction.

The Power Supply
----------------
You will be using your bench power supply to power your motor. Motors draw far too much current to be driving by the 5V logic of the USB and trying to draw this much power from the USB or your microcontroller would likely dammage both. In addtion, the motors run on higher voltages than are safe for your microcontroller. For these reasons, you need to be very careful about adding the bench power to your circuit. 

#. Turn on the power supply and set the voltage to 8 volts. 
# Turn off the power supply.
#. Using leads with alligator clips connect the bench supply to your circuit.

   #. Connect the black lead to the black or ground socket on your bench supply.
   #. Using a long jumpwire connect the alligator clip of the black lead to the ground bus of your breadboard. Normally when using two power supplies, you need to connect the grounds of both power supplies together.






