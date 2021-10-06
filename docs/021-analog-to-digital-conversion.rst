Analog To Digital Conversion
============================

Overview
--------

The potentiometer you learned about in the previous section represents your first introduction to an analog signal. An analog signal is one 
that varies infinitely over time. As you saw with your multimeter, the potentiometer can be used to produce ANY voltage between zero and
five volts on your device. This is in contrast to the button which can only produce two distinct voltage levels, zero volts or five volts. 

Your microcontroller has two types of input pins, digital and analog. The digital pins are assigned D0 - D13 and the analog pins are assigned A0 - A5. 
While these pins have very different uses, it may help to understand them better if we consider then only different by degree. Digital pins can represent
voltages as one of only two states, either 0 (LOW) or 1 (HIGH) regardless of the voltage input. The datasheet for your device states that any 
voltage between 0V and 1.5V will be presented as a 0 (LOW) and any voltage between 3V and 5V will be repsented as a 1 (HIGH). Voltages inbetween are 
indeterminate, but will be represented as either 0 or 1. 

You could use a potentiomenter with a digital pin instead of a button, but it would not be all that useful since it would only represent either a 0 or 1
over the whole range of the potentiometer.

By comparison, an analog pin can read 1024 different states (0 - 1023) instead of just two, based on the voltage input. The analog ports divide voltage input into much 
finer increments. A voltage of 0V to .005V would be represented as a 0, .005V to .010V would be represented as a 1, .010V to .015V would be represented as a 2 and so on to 
1023. This makes analog ports much more useful with potentiometers. While the analog port (ADC) can not read an infinite varation of voltages produced by a potentiometer, it can
read 1023 different states.

.. figure:: images/image122.png
   :alt: 

The diagram below shows more detail about how an analog voltage would be converted to number on the analog port (ADC) of your
microcontroller. You can read more about analog conversion in
analog section of
`concepts <https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.kxihcorejof7>`__.

.. figure:: images/image109.png
   :alt: 

Code
----

In order to use the analog to digital converter (ADC) on your Metro Mini
you will need to use the following command.

.. figure:: images/image99.png
   :alt: 

Exercise
~~~~~~~~

1. **Reading a Potentiometer**: Add a potentiometer to your board if you do not already have one set up. See the 
   previous section for how to set up a potentiometer. Connect the output of your potentiometers to an ADC port on
   your microcontroller. Remember there are five ADC ports (A0 - A5). 
   
2. Use the command above to read a value from this port. Make sure to place this line in your code where
   it will be read continously. 
   
3. Display the value from your potentiometer in a column on your serial monitor.  Note this value is stored 
   in the variable x. You will need a serial command to print the value of the variable in your serial monitor. The
   value you see should range from 0 to 1023 proportional to how you turn the potentiometer.

4. TEACHER CHECK \_\_\_\_

1. **Converting the reading from the potentiometer to voltage**: As you learned with your multimeter, when you turn the potentiometer
   the voltage output changes from 0 to 5 volts. As you saw above, your microcontroller converts this voltage to the numbers 0 to
   1023. In this challenge, you will convert the numbers 0 to 1023 back into the voltages that the represent.
   
2. Complete the following table in your notebook by calculating the volts per step for the 
   last two rows. In row 2 imagine that your ADC only has 10 possible states. The last row represents the 
   ADC on your microcontroller which has 1024 possible states. 

.. figure:: images/image17.png
   :alt: 

+---------------+----------------+---------+------------------+
| Low Voltage   | High Voltage   | Steps   | Volts per Step   |
+---------------+----------------+---------+------------------+
| 0 Volts       | 6 Volts        | 3       | 2 Volts/Step     |
+---------------+----------------+---------+------------------+
| 0 Volts       | 5 Volts        | 10      |                  |
+---------------+----------------+---------+------------------+
| 0 Volts       | 5 Volts        | 1024    |                  |
+---------------+----------------+---------+------------------+

TEACHER CHECK \_\_\_\_

3. Following the steps below, modify your code to display the voltage at the output from your
   potentiometer. 

   a. Copy the conversion factor from the last row of the table above. (i.e. How many
   volts is each step of the A/D converter)
   
   b. In your code multiply this factor by the results of the A/D
   converter. (i.e. if you are using the variable x to store the results
   of the A/D conversion than you would multiply this number by the
   conversion factor from above before printing the result). You can
   find information about how to multiply a variable
   `here <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.j1vujjth5hql&sa=D&ust=1587613173936000>`__.
   
   c. If you did this correctly, you should see the results vary between 0
   and 5 (or maybe just 4 depending on your potentiometer) representing
   the voltage produced by your potentiometer.

   TEACHER CHECK \_\_\_\_

   d. The voltage range 0 - 5 is a very crude representation of the
   voltage. Modify your code to display a voltage to a hundredth of a
   volt (2 decimal places).

   c. In order to store a number with a range of less than one (2 decimal
   place) you will need to initialize your variable as a
   `float <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.86fwcjklmgvf&sa=D&ust=1587613173937000>`__ instead
   of an int.
   
   d. Confirm you results by connecting a multimeter to the output of your
   potentiometer and measuring voltage while at the same time reading the results in your serial monitor. The results from the multimeter
   should match fairly closely the results in your serial monitor.

TEACHER CHECK \_\_\_\_
