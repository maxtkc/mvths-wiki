Review Challenge
================

Challenge:
----------

1. Set up a circuit to drive a piezo speaker with volume control. Use a `for
   loop <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.2u7q6orum403&sa=D&ust=1587613173962000>`__ to
   change the value of the tone over time. The tone could either rise or fall over time as the for loop increments or decrements. Make sure to use some 
   delay in your for loop so that each tone is played for a period of time.

TEACHER CHECK \_\_\_\_

2. Modify your code so that frequency in your tone function remains the same, but 
   the duration of the tone (the delay) is changed as the for loop increments or decrements.

TEACHER CHECK \_\_\_\_

3. Add a second potentiometer to your circuit. This one should be connected in the conventional manner and attached to an analog port. Write a program so that
   the frequency of the tone played on your piezo speaker changes as you turn the potetiometer. Note that the analogRead() function on produces a range of values
   between 0 and 1023 which as frequencies is in the range of human hearing. You may want to use math to increase or otherwise alter this range.

TEACHER CHECK \_\_\_\_

4. Set up a circuit that can play three different tones based on which
   button you press. Each button should play a different tone.

TEACHER CHECK \_\_\_\_
