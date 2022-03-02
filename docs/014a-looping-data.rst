The Loop Function
=================

Overview
---------
As you may have noticed there are two functions *void setup()* and *void loop()* in every code file you create using the Arduino IDE. Up until now you have always placed your code inside the *void setup()* function. Code inside the *void setup()* function runs exactly once after the program is started or your Metro Mini is plugged into power. Code inside *void loop()* function runs repeatedly until the Metro Mini is unplugged. 

As a reminder, in order to place code inside of either the *void setup()* or *void loop()* function, you must place your code between the open and closed curly braces for that function. Every function in C is required to have an open and close curly brace to define the contents of the function.

.. code-block:: c

   void loop() { //open curly brace

     //All code inside of the loop function must be placed between these
     //two curly braces.

   } // closed curly brace

Exercise:
~~~~~~~~~

Repeat the steps above for sending the word "cat" to your terminal window, but instead of placing your Serial.print() command in the setup function, place it in the loop function. **IMPORTANT:** Make sure to add a delay of at least 100ms to your loop function. This will ensure that the program does not try to send data too quickly to the serial port and CRASH the Arduino IDE.

TEACHER CHECK \_\_\_\_\_



