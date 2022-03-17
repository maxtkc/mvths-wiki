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

#. Add an LED to your board. 

NOTE: If your circuit is not reliable (i.e. not consistently changing states), you might need a delay after your button press that is longer than the average time of a button press. This will ensure that your code is not continually checking the state of a button while it is pressed.

4. TEACHER CHECK \_\_\_\_


There are basically two methods in software for reading a button press. One is **direct state control** in which the state of the button equals the state of the device. For example, a direct state control of an LED would turn the LED on when the button is pressed and off when the button is not pressed. The second is **toggle state control**, in which the button can transition a device between two states. For example in toggle state control of an LED, the LED would change its state (on or off) after each button press.
