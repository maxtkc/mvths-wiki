Review Challenge
================

Challenge:
----------

#. Set up a circuit to drive a piezo speaker with volume control. Use a for loop to change the value of the tone over time. The tone could either rise or fall over time as the variable used in the for loop increments or decrements. Make sure to use some delay in your for loop so that each tone is played for a period of time.

   TEACHER CHECK \_\_\_\_

#. Modify your code so that it produces a fixed frequency. Choose any frequency you like. Now change the duration of the tone (the delay) over time. Specifically, use the variable in the for loop to change the duration of the delay used to set the duration of the tone. Additionally, you will need to turn the tone off and provide another delay, i.e. the tone will turn on for a period of time (delay) and off for a period of time (delay).

   TEACHER CHECK \_\_\_\_

#. Add a second potentiometer to your circuit. This one should be connected in the conventional manner and attached to an analog port. Write a program so that the frequency of the tone played on your piezo speaker changes as you turn the potetiometer. Note that the analogRead() function on produces a range of values between 0 and 1023. Check out the table showing frequencies and notes to determine which notes you will hear. You may want to use math to increase or otherwise alter this range.

   TEACHER CHECK \_\_\_\_

#. Set up a circuit that can play three different tones based on which button you press. Each button should play a different tone.

   TEACHER CHECK \_\_\_\_
