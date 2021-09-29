Potentiometers
==============

Overview
--------

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
of resistance between A and B is fixed) and is based on the length of the resistive element between A and B. The wiper (W) shorts the
resistor, so the distance between W and A (and W and B) varies as the wiper is turned. Resistance is based on the distance between W and A.
A shorter distance results in less resistance between these two points. Note that the resistance value between W and B is the inverse
of the resistance value between W and A.

|image0|\ |image1|

On the right is a schematic symbol for a potentiometer. Note the three leads marked A, B and W. Connecting pins
A and B to 5V and ground (the order does not matter) creates what is called a voltage
divider. This allows the voltage measured at W (between W and gound) to vary between the high voltage on your circuit (5 Volts) and ground.

Exercise
~~~~~~~~

Construct the following circuit on your breadboard and measure at W (output). This will require you to use a multimeter. Remember to measure voltate at a point in 
your circuit you need to use your multimeter to measure between that point and ground. If you need help refer back to the 
section on multimeter. Record the highest and lowest voltage by turning the
potentiometer all the way to the right or left. Since you will need to measure two points and move the potentiometer, I recommend using alligator leads with your multimeter so your hands are free to turn the potentiometer.

https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=kix.53hctxuwjhmw

.. figure:: images/image60.png
   :alt: 

+-------------------+------------------------+
|                   | Potentiometer Output   |
+-------------------+------------------------+
| Highest Voltage   |                        |
+-------------------+------------------------+
| Lowest Voltage    |                        |
+-------------------+------------------------+

1. TEACHER CHECK \_\_\_\_

.. |image0| image:: images/image71.png
.. |image1| image:: images/image57.png
