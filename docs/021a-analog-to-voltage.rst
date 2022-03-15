Analog To Voltage Conversion
============================

Overview
--------
In this lesson you will combine what you learned in the previous lesson on analog to digital conversion and scaling to create a simple voltmeter. Since microcontrollers are inherently digital devices any voltage range must be converted into a finite number of steps. In the following diagram a range of 0V to 6V is divided into 3 steps with each step representing two volts.

.. figure:: images/steps.png
   :alt: 

Exercise
~~~~~~~~

#. Set up your potentiometer as described in the section on potentiometers. Measure the voltage output using a multimeter.
   
#. Complete the following table in your notebook. The two columns represent a source range and the steps column represent a target range. Using the formula you learned in the previous lesson, you can find the Volts per step, or conversion factor. Note that the last row represents the actual values of your microcontroler. The range for your potentiometer is 0V to 5V and the analog converter on your microcontroller has a range of 1024 steps. Round your answers to the nearest 1000th. 

   +---------------+----------------+---------+------------------+
   | Low Voltage   | High Voltage   | Steps   | Volts per Step   |
   +---------------+----------------+---------+------------------+
   | 0 Volts       | 6 Volts        | 3       | 2 Volts/Step     |
   +---------------+----------------+---------+------------------+
   | 0 Volts       | 8 Volts        | 10      |                  |
   +---------------+----------------+---------+------------------+
   | 0 Volts       | 5 Volts        | 35      |                  |
   +---------------+----------------+---------+------------------+
   | 0 Volts       | 5 Volts        | 200     |                  |
   +---------------+----------------+---------+------------------+
   | 0 Volts       | 5 Volts        | 1024    |                  |
   +---------------+----------------+---------+------------------+

   TEACHER CHECK \_\_\_\_

#. Following the steps below to create a voltmeter. 

   #. Connect the output of your potentiometer to an analog port on your microcontroller or Arduino. 
   
   #. Write a program to display the value of the potentiometer in your terminal window. You should see a range of 0 to 1023 as you turn the potentiometer.
   
   #. Multiply the value from your potentiometer by the steps (conversion factor) you calculated in the last column of the last row above. Print this number in your terminal window.
   
  
   
   #. If you did this correctly, you should see the results vary between 0
   and 5 (or maybe just 4 depending on your potentiometer) representing
   the voltage produced by your potentiometer.

   TEACHER CHECK \_\_\_\_

   d. The voltage range 0 - 5 is a very crude representation of the
   voltage. Following the steps below, modify your code to display a voltage to a hundredth of a
   volt (2 decimal places).

   c. In order to store a number with a range of less than one (2 decimal
   place) you will need to initialize your variable as a
   `float <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.86fwcjklmgvf&sa=D&ust=1587613173937000>`__ instead
   of an int.
   
   d. Confirm you results by connecting a multimeter to the output of your
   potentiometer and measuring voltage while at the same time reading the results in your serial monitor. The results from the multimeter
   should match fairly closely the results in your serial monitor.

TEACHER CHECK \_\_\_\_
