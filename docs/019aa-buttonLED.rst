Button and LEDs
=======

Overview
--------

In this lesson you will use a button to turn on an LED. But unlike in previous examples, you will not directly control the LED with the button. Your button will communicate with your microcontroller which will in turn communicate with your LED.

Exercise:
~~~~~~~~~

#. Set pin 7 as input.

#. Connect the output from your button (the point at which you measured voltage in the previous section) to the pin 7.

#. Write a program to read the value of the button and display it in your serial monitor. Below is the function you can use to read a value on pin 7 and place it into the variable x. The value of x should be displayed continuously in a column in your serial monitor.

   .. code:: C
      
      x = digitalRead(7); // Read the value on pin 7 and place the result in x
      
#. In your notebook write the value of x when the button is pressed and the value of x when the button is not pressed.

   TEACHER CHECK ___
   
#. Modify your code to display the word "press" when the button is pressed and "notpress" when the button is not pressed. You may have to refer to the lesson Input Pins for help with the code.

     TEACHER CHECK ___
     
#. Add an LED to your circuit. **REMEMBER** to include a resistor with your LED.

#. Write a program to flash the LED.

   TEACHER CHECK \_\_\_\_

#. Modify your code to turn on the LED when the button is pressed and off when the button is not pressed.
