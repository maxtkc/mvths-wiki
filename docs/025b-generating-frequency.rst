Generating Frequencies
==========================

Overview
--------

In the previous sections you learned about frequency and period and how to convert between the two.  In this lesson you will learn how to use the conversion formulas to generate specific frequencies using your microcontroller and the following steps.

#. Convert frequency to period: The first step in generating a frequency is find the period of this frequency using the conversion formula from the previous section of 1/f = T. Again f stands for frequency and T stands for period. For example: 

   ::

      1/1382Hz = 0.000723589s
   
#. Divide the period in half: The period of a wave is equal the sum of one high pulse and one low pulse. In your code, you need two delays. One for the length of the high pulse and one for the length of the low pulse. For now we will assume these two delays are always equal. 

   ::

      0.000723589s/2 = 0.0003617945s

#. Convert seconds to us or ms: The next step is creating a delay in either ms or us. You have two options for delay functions. delay() takes values milliseconds. delayMicroseconds() takes values in microseconds. The following is a conversion from seconds to milliseconds. 

   ::

      0.0003617945s = 0.3617945ms

   From the lesson on the delay function we know that it only takes whole numbers, so will need to use the function delayMicroseconds() and now convert the milliseconds tomicroseconds. 
   
   ::

      0.3617945ms = 361.7945us

Since the delayMicroseconds() function also only takes whole numbers we will need to round our result.

   ::

      361.7945us rounds to 362us. 

Now we can use the resulting times for the two delays in our loop. 

Exercise:
~~~~~~~~~

Complete the table below in your notebook. Write a program to generate each frequency and measure the frequency with your multimeter to confirm. Note 
that on the multimeter there is position labeled with Hz (Hertz) for frequency. You can tell you are on the correct setting if you see Hz on the screeen. 
Again, connect the black lead to ground and the red lead to the pin you are measuring. Demonstrate
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



