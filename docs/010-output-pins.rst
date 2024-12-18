Output Pins
===========

Overview
--------

The first code you are going to write for your microcontroller will be used to control the pins on the microcontroller. The digital pins on your microcontroller (mentioned above) can be set  as either inputs or outputs. As an output, the voltage on the pin can be set to either HIGH (5V) or LOW (0V). A pin set as an output can be used to control an LED, a speaker, a motor or just about any sort of electronic device. As an input, the voltage from another device can be read on the pin. A pin set as an input can be used to read value from a sensor or potentiometer.

Exercise:
~~~~~~~~~

In this first exercise, you will set one of the pins of your microcontroller as an output pin and then set that pin to HIGH.

#. Open a new code file (File/New) in your Arduino IDE.

#. Type the following two lines of code inside your *void setup()* function. The first line sets pin 8 on your microcontroller as an output pin. The second line sets the value of pin 8 to HIGH. **IMPORTANT** All text after a // is a comment. These are simply notes inside the code and are NOT compiled with the code. You can leave anything after // out of your code and it will not change how the code functions. Comments are useful for making your code more readable and you will be encouraged to use them as you write more complex code.
   
   .. code-block:: c
   
      pinMode(8, OUTPUT);  // Set pin 8 to an output pin
   
      digitalWrite(8, HIGH); // Set pin 8 to 1 (or HIGH)
      
 **Important:** In order to place code inside of either the *void setup()* or *loop()* function, you must place your code between the open **{** and closed **}** curly braces for that function. Every function in C is required to have an open and close curly brace to define the contents of the function.

   .. code-block:: c

     void setup() { //open curly brace

          //All code inside of the setup function must be placed between these
          //two curly braces.

     } // closed curly brace

#. Compile and upload your code. If you have errors, ask your teacher for help.

#. Use a multimeter to confirm that the voltage on pin 8 is 5V (or close to 5V). Connect the black lead to ground on your circuit and touch the red lead to pin 8 on your Metro Mini. 
   
   TEACHER CHECK \_\_\_\_\_

#. Modify your code to set pin 8 to 0V (LOW).

#. Program your microcontroller and confirm with a multimeter.

   TEACHER CHECK \_\_\_\_\_

#. Modify your code to set pin 6 to 5V. Program and confirm with your multimeter.

   TEACHER CHECK \_\_\_\_\_
