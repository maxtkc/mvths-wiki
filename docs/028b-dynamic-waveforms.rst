Dynamic Waveforms
=========================

Overview
--------

In this lesson, using a for loop you will create waves that change over time, display them on your scope and listen to them on a piezo speaker. 

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

2. Add a piezo speaker with volume control to your breadboard, and drive the speaker with this waveform.

TEACHER CHECK \_\_\_\_\_

3. Modify your code to include a for loop around your pulse code. The for loop should start a zero and count to 400. The variable used in your for loop
   should be the same variable as used in the delay for the "high" portion of your pulse. As in, the high portion of your pulse should vary between 0us and 
   400us over time while the low portion remains at 400us. Display this on your scope as well with your piezo speaker.
  
TEACHER CHECK \_\_\_\_\_

4. Play around with changing your waveform to make different sounds and displaying them on your scope.
