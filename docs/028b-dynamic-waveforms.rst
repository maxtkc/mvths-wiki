Dynamic Waveforms
=========================

Overview
--------

In this lesson, you will create waves that change over time, display them on your scope and listen to them on a piezo speaker. 

Exercise:
~~~~~~~~~

#. Write a program that creates a waveform, but instead of using fixed values for the delay values (HIGH and LOW) use a two variables. See example below. Initialize these variables at the top of your code. Set both to 400.  Make sure to use *delayMicroseconds()* for your two delays. Display your waveform on your scope. 

.. code-block:: C

   delayMicroseconds(400); //Fixed 400us delay

.. code-block:: C

   delayMicroseconds(x); //A variable delay based on the value of x

#. Add a piezo speaker with volume control to your breadboard, and drive the speaker with this waveform.

   TEACHER CHECK \_\_\_\_\_

#. Modify your code to include a for loop to control one of the delays. Set up your code so the for loop controls one of the delays over time. Display this on your scope as well with your piezo speaker.
  
   TEACHER CHECK \_\_\_\_\_

#. Play around with changing your waveform to make different sounds and displaying them on your scope.
