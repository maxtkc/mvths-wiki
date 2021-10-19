Generating Frequencies
==========================

Overview
--------

In the previous sections you learned about frequency and period and how to convert between the two. In this lesson you will learn how to use the conversion formulas to generate
specific frequencies using your microcontroller. The first step in generating a frequency of 1382Hz is find the period of this frequency using the conversion formula from
the previous section of 1/f = T. Again f stands for frequency and T stands for period. 

1/1382Hz = 0.000723589s

Remember that Hertz is a unit of cycles (or period) per second, so the result of our conversion is seconds. This period is the measure of one cycle or period as shown in
the diagram below. 

.. figure:: images/waveforms-tim3.png
   :alt: 

But note that the cycle or pulse in your code is made up of two delays. One is for the high part of the pulse and the other is for the low part of the pulse.
Since these two delays make up the period, you will need to divide the period in half. One half of the period will be the delay for the high part of the pulse
and one half of the delay will be the period for the low part of the pulse. For now we will assume these two delays are always equal, but in future lessons you will how making them unequal can be useful.

0.000723589s/2 = 0.0003617945s

The next step is creating a delay of .0003617945. As know the delay function takes an argument in milliseconds not seconds so a first step is convert the seconds to 
milliseconds. Check the lesson on engineering notation if you need help with this conversion.

0.0003617945s = 0.3617945ms

From the lesson on the delay function we know that it only takes whole numbers, so will need to use the function delayMicroseconds() and now convert the milliseconds to
microseconds. Again, check the lesson on engineering notation for help with this conversion.

0.3617945ms = 361.7945us

Since the delayMicroseconds function also only takes whole numbers we will need to round our result.

361.7945us rounds to 362us. 

Now we can use the resulting times for the two delays in our loop. 

Exercise:
~~~~~~~~~

Complete the table below in your notebook. Write a program to generate each frequency and measure the frequency with your multimeter to confirm. Demonstrate
one of these frequencies for your teacher. 


.. list-table:: Generating Frequencies
   :widths: 25 25 50
   :header-rows: 1

   * - Frequency
     - Period (seconds)
     - Delay value (us)
   * - 345Hz
     - 
     - 
   * - 2876Hz
     - 
     - 
   * - 879Hz
     - 
     - 
   * - 1390Hz
     - 
     - 
  
TEACHER CHECK \_\_\_\_\_



