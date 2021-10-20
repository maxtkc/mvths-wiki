Changing Waveforms
=========================

Overview
--------

In this lesson, using a for loop and a potentiometer you will create waves that move over time, display them on your scope and listen to them on a piezo speaker. 

Exercise:
~~~~~~~~~

1. Write a program that creates a waveform that has a period of 800us with the high portion of the pulse lasting for 400us and the low portion of the 
   pulse lasting for 400us. But instead of setting each of the delays as a fixed number as shown below, I want you to use a variable as your delay value as in
   following example. You should use a different variable for each of the two delays. Initialize each of your variables to 400. Display your waveform on your scope.

.. code-block:: C

  delayMicroseconds(400); //Fixed 400us delay

.. code-block:: C

  delayMicroseconds(x); //A variable delay based on the value of x
  
TEACHER CHECK \_\_\_\_\_
