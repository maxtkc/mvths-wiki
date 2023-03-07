Sumo Line Software
======================

Overview
--------

In this lesson, you will learn how to write a program to accurately control your line sensor. There are three possible methods for reading the output from this sensor. One is using the analog port, the second is using a digital port, the third is using an external comparitor. Each method is described below and their pros and cons.

- **Analog**: Since this sensor produces an analog signal, you can read the output on any analog port which will provide a reading from 0 to 1023. Reading the value on an analog port provides an easy way to set and adjust the exact threshold for sensing a line. The downside of the using the analog port is that reading values is slow and you can not easily integrate an interrupt. The following is a method for testing the sensor using an analog port.

    - Using the data you collected in the previous lesson for serial monitor values over black and white surfaces, write a program that displays in the terminal window the word "white" when the sensor is over a white surface and "black" when the sensor is over a black surface.

- **Digital**: This method relies on the internal comparator on each of the digital pins. Since you can not adjust the threshold in software you must rely on setting the correct height to get the results you want. The advantage of this method is that it is fast and can be used with interrupts.

   - Repeat the last exercise, but move the output from an analog port to a digital port. You might need to adjust the height of your sensor so that it works correctly.

- **Comparator**: This is method provides the most accurate results and allows you to adjust easily for changes in ambient light or changes in the surface you are detecting. It also allows you to use interrupts in your code. The downside is that it requires a more complex circuit. 

Exercise
--------

#. Refer to the section on `comparator <https://mvths-wiki.readthedocs.io/en/latest/065-comparator.html>`__. 

#. Construct this exact circuit including the LED, but connect the output of your line sensor to Vi instead of the light sensor and resistor shown in the circuit. 

#. Connect Vo to a digital pin on your microcontroller board.




