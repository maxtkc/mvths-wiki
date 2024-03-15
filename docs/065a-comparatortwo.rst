Comparator Two
==========

Overview
--------
The following circuit shows a compartor being used in circuit. Note that the Vref is being controlled by a potentiometer. This way, it is easy to set the threshold voltage to any value between 0 V and 5 V. In this circuit the Vi is being controlled by a resistive light sensor as you have seen in previous lessons. The voltage on Vi changes depending on the amount of light that falls on the sensor. The Vo is tied to an LED, so you can easily and visually determine if the threshold voltage has been tripped. 

.. figure:: images/LM339circuit.PNG
   :width: 400
   :alt:
   

   
Exercise
--------

#. Construct the circuit shown above using an LM339. 

#. Adjust the potentiomater so that the LED turns on when the sensor is in bright light.

#. Now set up circuit so that the LED turns on when the sensor is in the dark. You can do this by swaping the the Vi (or -) input with the Vref (or +) input. 

#. Connect Vo of your circuit to a digital pin on your microcontroler. Do not remove the LED part of the circuit. This will be useful for confirming if your software is working correctly. 

#. Write a program to that displays the word "light" in your serial monitor when the sensor detects a bright light and "dark" when the sensor does not detect a bright light.
