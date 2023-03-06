Sumo Line Sensor
======================

Overview
--------

In this lesson, you will learn how to use a QTR-MD-01A Reflectance Sensor to distinguish between light and dark surfaces. Specifically, this sensor will be used to detect the white line on the outside of the sumo ring.

.. image:: images/sumoring.PNG
      :width: 400px

The QTR-MD-01A sensor (shown below) includes a photo emitter and sensor pair as well as well as other necessary components. The schematic for the sensor is shown below as well. On the left side of the schematic is the IR emitter which sends out infrared light. On the right of the schematic is the phototransistor which senses infrared light. The voltage at the OUT pin varies depending on how much infrared light is reflected from the IR emitter. You can check out the `product page <https://www.pololu.com/product/2458>`__  for additional information. 

.. image:: images/linesensor.PNG
      :width: 400px

.. image:: images/linesensorschematic.PNG
      :width: 400px


In order to accurately test this sensor, you will need to create a sensor mount, a connector cable and a test card. The sensor mount should hold the sensor at a fixed height around 0.125” (3mm) above the table and allow you to easily pass the test card under the sensor. You can create this using cardboard and tape. Since the sensor will not be on your breadboard, you will also need to use flexible jump wires to connect it to your board. Finally, you will need to create a card for testing your sensor’s sensitivity to dark and light surfaces. This can be made simply from a white index card with a single black line made using a marker or tape.

There are three possible methods for reading the output from this sensor; analog, digital and comparator. Each method is described below and their pros and cons.

- **Analog**: Since this sensor produces an analog signal, you can read the output on any analog port which will provide a reading from 0 to 1023. Reading the value on an analog port provides an easy way to set and adjust the exact threshold for sensing a line. The downside of the using the analog port is that reading values is slow and you can not easily integrate an interrupt. The following is a method for testing the sensor using an analog port.

  #. Connect the sensor mount to your breadboard using the three wire cable you created in the exercise above. Set the sensor on the table and place your test card under the sensor. Use a multimeter to measure the voltage at the output of the sensor. The voltage should vary depending on the whether the dark line or white card is under the sensor.

     - Lowest value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Volts (white background)

     - Highest value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Volts (black line)

  #. Create a circuit that can detect if the sensor is over the white background or black line. Connect the output of the sensor to an analog port. Write a program that displays in the terminal window the word “line” when the sensor is over the black line and “background” when the sensor is over the white background.

- **Digital**: This method relies on the internal comparator on each of the digital pins. Since you can not adjust the threshold in software you must rely on setting the correct height to get the results you want. The advantage of this method is that it is fast and can be used with interrupts.

  Repeat the last exercise, but move the output from an analog port to a digital port. You might need to adjust the height of your sensor so that it works correctly.

- **Comparator**: This is method provides the most accurate results and allows you to adjust easily for changes in ambient light or changes in the surface you are detecting. It also allows you to use interrupts in your code. The downside is that it requires a more complex circuit. Using what you learned in the section on comparators design a circuit that reads the output of the sensor. Include a potentiometer to set the reference voltage.

.. |image0| image:: images/image49.png
.. |image1| image:: images/image30.png
.. |image2| image:: images/image11.png
.. |image3| image:: images/image87.png
