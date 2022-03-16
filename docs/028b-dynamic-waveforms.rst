Dynamic Waveforms
=========================

Overview
--------

In this lesson, you will create waves that change over time, display them on your scope and listen to them on a piezo speaker. 

Exercise:
~~~~~~~~~

#. Write a program that creates a waveform that has a period of 800us with the high portion of the pulse lasting for 400us and the low portion of the pulse lasting for 400us. But instead of setting each of the delays as a fixed number in the first example below, use a variable as your delay value as in the second example below. You should use a different variable for each of the two delays. Initialize each of your variables to 400. Display your waveform on your scope.

.. code-block:: C

   delayMicroseconds(400); //Fixed 400us delay

.. code-block:: C

   delayMicroseconds(x); //A variable delay based on the value of x

#. Add a piezo speaker with volume control to your breadboard, and drive the speaker with this waveform.

   TEACHER CHECK \_\_\_\_\_

#. Modify your code to include a for loop to control one of the delays. Set up your code so the for loop controls one of the delays over time. Display this on your scope as well with your piezo speaker.
  
   TEACHER CHECK \_\_\_\_\_

#. Play around with changing your waveform to make different sounds and displaying them on your scope.
