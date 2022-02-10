Output Pins
===========

Overview
--------

The digital pins on your microcontroller (mentioned above) can be set  as either inputs or outputs. As an output, the voltage on the pin can be set to either HIGH (5V) or LOW (0V). A pin set as an output can be used to control an LED, a speaker, a motor or just about any sort of electronic device. As an input, the voltage from another device can be read on the pin. A pin set as an input can be used to read value from a sensor or potentiometer.

Exercise:
~~~~~~~~~

In this first exercise, you will set one of the pins of your microcontroller as an output pin and then set that pin to HIGH.

#. Open a new code file (File/New) in your Arduino IDE.

#. Type the following two lines of code inside your setup. The first line sets pin 8 on your microcontroller as an output pin. The second line sets the value of pin 8 to HIGH.
   
   .. code-block:: c
   
      pinMode(8, OUTPUT);
   
      digitalWrite(8, HIGH);

#. Compile and download your code. If you have errors, ask your teacher for help.

#. Use a multimeter to confirm that the voltage on pin 8 is 5V (or close to 5V). Connect the black lead to ground on your circuit and touch the red lead to pin 8 on your Metro Mini. 
   
   TEACHER CHECK \_\_\_\_\_

#. Modify your code to set pin 8 to 0V (LOW).

#. Program your microcontroller and confirm with a multimeter.

   TEACHER CHECK \_\_\_\_\_

#. Modify your code to set pin 6 to 5V. Program and confirm with your multimeter.

   TEACHER CHECK \_\_\_\_\_
