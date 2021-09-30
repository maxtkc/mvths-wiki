Analog To Digital Conversion
============================

Overview
--------

The potentiometer you learned about in the previous section represents your first introduction to an analog signal. An analog signal is one 
that varies infinitely over time. As you saw with your multimeter, the potentiometer can be used to produce ANY voltage between zero and
five volts on your device. This is in contrast to the button which can only produce two distinct voltage levels, zero volts or five volts. 

The button is considered a binary device. The prefix bi means two. The button only has two states, either on (5 volts) or off (0 volts). This makes
it perfectly compatible with a microcontroller or any computing device. Computing devices store ALL information from data used to represent a single 
letter to a full-length movie in millions of transistors which each are capable of respesently only two states on or off. In the case of your microcontroller
they are represented as 0 Volts (off) and 5 Volts (on).

In order for your microcontroller to make use of an analog signal, it must first be converted to a digital signal.
The microcontroller on the Metro Mini has an internal analog to digital
converter (ADC) which is accessible on six pins labeled A0 through A5.

The ADC has 1024 states so that any analog voltage applied to an ADC pin
is converted to one of 1024 different states.

.. figure:: images/image122.png
   :alt: 

For example, if your analog device had a voltage range of 0 volts to 5
volts than 0 volts would correspond to a state of 0 and 5 volts would
correspond to a state of 1023, and each voltage level in between would
correspond to exactly one of the 1024 states (0 - 1023). The diagram
below shows an example. You can read more about analog conversion in
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

1. Add a potentiometer to your board if you do not already have one set up. See the 
   previous section for how to set up a potentiometer. Connect the output of your potentiometers to an ADC port on
   your microcontroller. Remember there are five ADC ports (A0 - A5). Use the command above to read a value 
   from this port and display the value in a column on your serial monitor. The
   value should range from 0 to 1023.

2. TEACHER CHECK \_\_\_\_

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
   volts is each step of the A/D converter): \_\_\_\_\_
   
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
