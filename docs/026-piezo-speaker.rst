Piezo Speaker
=============

Overview
--------

In this lesson you will use what you learned about frequency to make music with a piezo speaker. Piezo speakers are found in lots of common devices such as microwave ovens and cell phones and can be used to tell you if you have a phone call, let you know your pizza is hot or to confirm you pressed a button.

Piezo speakers are normally formed around two metal plates as shown in the picture on the left. The picture on the right shows a piezo speaker in a secure plastic housing.

.. figure:: images/image42.png
   :alt: 

The sound from a piezo speaker results from applying a voltage to the piezoelectric material which in turn causes a vibration. This high frequency vibration results in a sound or note. The following shows a  piezo speaker at rest (low pulse) and under voltage (high pulse).  

.. figure:: images/image32.png
   :alt: 

Driving a piezo speaker only requires a single pin that can produce a pulse. While it is possible to drive a piezo speaker directly, they tend to be very loud so it is useful to add a potentiometer to the circuit as a volume control, as shown in the circuit below.

IMPORTANT: In the schematic below the potentiometer is not being used as a voltage divider to provide input to an analog pin on your microcontroller, as in previous circuits. make sure to set up your circuit exactly as shown below.

Exercise
~~~~~~~~

1. Construct the following circuit and connect the pulse lead (TO MCU) to any digital pin on your microcontroller pins. After you complete the circuit, write a program to drive your speaker with a frequency of 100 Hz. In order to determine the delays for your code, you will need to convert the frequency to a period. If you need help with this, you can refer to a previous lesson.

.. figure:: images/image111.png
   :alt: 

TEACHER CHECK \_\_\_\_

2. Modify your code to produce a frequency of 1000Hz. Note you will need
   to use a delayMicroseconds() in order to reach this frequency. Confirm the frequency with your multimeter.

TEACHER CHECK \_\_\_\_

3. What are the highest and lowest frequencies you can hear? These may
   be the highest or lowest you can play. Record your answers below.

+---------------------+--------------------+
| Highest Frequency   | Lowest Frequency   |
+---------------------+--------------------+
+---------------------+--------------------+

TEACHER CHECK \_\_\_\_

