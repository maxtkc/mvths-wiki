Analog To Voltage Conversion
============================

Overview
--------
In this lesson you will use what you learned in the previous lesson to convert a voltage to an analog value (0 - 1023) and then convert this value
back to voltage. In the following diagram a range of 0V to 6V is divided into 3 steps. How many volts does each step represent?


.. figure:: images/image17.png
   :alt: 

Exercise
~~~~~~~~

1. As you learned with your multimeter, when you turn the potentiometer dial
   the voltage output changes from 0 to 5 volts. As you saw above, your microcontroller converts this voltage to a range of values from 0 to
   1023. In this challenge, you will convert the numbers 0 to 1023 back into the voltages that the values represent.
   
2. The first step is understanding how to divide voltages into discrete steps. The first two columns of following table list a set of possible high and low
   voltages. The third column represents the number of steps of an analog converter. Assuming the voltage range given and the number of steps, determine
   the volts per step for each row and recorde the entire table in your notebook. Note that the last row represents the actual values of your 
   microcontroler with a high of 5 Volts. a low is 0 Volts, and 1024 steps.


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
