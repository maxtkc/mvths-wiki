Button Count
=============

Overview
--------

So far you have mostly used buttons as a way to directly control the state of your software. For example, you have used a button to turn on an LED when the button is pressed and off when the button is not pressed. In this lesson, you will learn to count the number of times a button is pressed. In this way, you can use the number of button presses to control the volume of the speaker, the brightness of an LED, or the number of LEDs visible.

Exercise
~~~~~~~~

#. Construct a circuit that includes a button as an input. Remember to use a resistor when setting up your button. 

#. Write a program to count the exact number of times the button is pressed and display this number in the terminal window.

   TEACHER CHECK \_\_\_\_

#. Modify your code so that the variable used for counting presses counts up to 10 and then starts back at 0. 

#. Add a 4-digit seven-segment display to your board. MAKE SURE TO DISCONNECT YOUR BOARD FROM POWER, before addting this component. MAKE SURE TO CORRECTLY CONNECT POWER AND GROUND for this component. Modify your code to display the button count value on the display.

#. Add an LED to your board. Modify your code to use analogWrite to change the brightness of your LED. The brightness should change from 0 for 0 presses to 255 for 10 presses.

TEACHER CHECK \_\_\_\_
