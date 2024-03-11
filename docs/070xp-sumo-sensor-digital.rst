STEP ELEVEN: Sumo Digital Sensor
======================

Overview
--------

In this lesson, you will learn how to write a program to control your sensor on a digital port.  This method relies on the internal comparator on each of the digital pins. Since you can not adjust the threshold in software you must rely on setting the correct height to get the results you want. The advantage of this method is that it is fast and can be used with interrupts.

Exercise
~~~~~~~~

#. Move the pin connecting OUT from the sensor to a digital port on your MetroMini. 
#. Write a program to that prints "white" in your serial monitor when a white refletive surface is below the sensor and "black" when a non-reflective surface is below your sensor.



