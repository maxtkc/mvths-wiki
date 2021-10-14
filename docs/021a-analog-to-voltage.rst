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
