Sumo Line Detector
======================

Overview
--------

In this lesson, you will learn how to use a QTR-MD-01A Reflectance Sensor with your robot. As you noted in the previous lesson, stray light can easily affect the signal value of your sensor. In order to get an accurate reading, you will need to mount this sensor at its optimal distance from the surface you are testing. 

Exercises
---------

#. Using materials such as cardboard or chipboard, create a mount for your sensor that keeps it about 5mm from the surface of your table. You may also want to shroud it from stray light. 

# Create a test card which includes a black and white surface. This can be done with an index card and tape, but note that not all white surfaces reflect eqaully and not all black surfaces reflect equally. Check out the surface of the sumo table as a reference.

#. Using your new set up, record voltage values in your notebook for the black and white surfaces.

   - White surface: ______
   
   - Black surface: ______
   
#. Now connect the output from your sensor to an analog port on your microcontroller. 

#. Write a program to display these values on your serial monitor.

#. Repeat the test above and record the values in your notebook from your serial monitor.

   - White surface: ______
   
   - Black surface: ______

There are three possible methods for reading the output from this sensor; analog, digital and comparator. Each method is described below and their pros and cons.

- **Analog**: Since this sensor produces an analog signal, you can read the output on any analog port which will provide a reading from 0 to 1023. Reading the value on an analog port provides an easy way to set and adjust the exact threshold for sensing a line. The downside of the using the analog port is that reading values is slow and you can not easily integrate an interrupt. The following is a method for testing the sensor using an analog port.

  #. Connect the sensor mount to your breadboard using the three wire cable you created in the exercise above. Set the sensor on the table and place your test card under the sensor. Use a multimeter to measure the voltage at the output of the sensor. The voltage should vary depending on the whether the dark line or white card is under the sensor.

     - Lowest value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Volts (white background)

     - Highest value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Volts (black line)

  #. Create a circuit that can detect if the sensor is over the white background or black line. Connect the output of the sensor to an analog port. Write a program that displays in the terminal window the word “line” when the sensor is over the black line and “background” when the sensor is over the white background.

- **Digital**: This method relies on the internal comparator on each of the digital pins. Since you can not adjust the threshold in software you must rely on setting the correct height to get the results you want. The advantage of this method is that it is fast and can be used with interrupts.

  Repeat the last exercise, but move the output from an analog port to a digital port. You might need to adjust the height of your sensor so that it works correctly.

- **Comparator**: This is method provides the most accurate results and allows you to adjust easily for changes in ambient light or changes in the surface you are detecting. It also allows you to use interrupts in your code. The downside is that it requires a more complex circuit. Using what you learned in the section on comparators design a circuit that reads the output of the sensor. Include a potentiometer to set the reference voltage.

.. image:: images/sumoring.PNG
      :width: 400px

