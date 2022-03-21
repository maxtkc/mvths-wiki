Button and LEDs
=======

Overview
--------

In this lesson you will use a button to turn on an LED. But unlike in previous examples, you will not directly control the LED with the button. Your button will communicate with your microcontroller which will in turn communicate with your LED.

Exercise:
~~~~~~~~~

#. Set pin 7 as input.

#. Connect the output from your button (set up in the previous section) to the pin 7.

#. Write a program to read the value of the button and display it in your serial monitor. Below is the function you can use to read a value on pin 7 and place it into the variable x. This function should be in your loop so that it is read continually. If you need to review the reading an input check the previous lesson Input Pins.

   .. code:: C
      
      x = digitalRead(7);

  
#. Add an LED to your microcontroller and write a program to confirm that you can turn it on and off. **REMEMBER** to include a resistor with your LED.

#. Add a button to your microcontroller on a different pin. Confirm in software that your micrcontroller can read the value of the button. This could be done in the terminal window with a serial command.

#. Write a program to read the value of the button press (either HIGH or LOW) and turn on the LED when the button is pressed. You might need to review the code under lesson Inputs.

TEACHER CHECK \_\_\_\_
