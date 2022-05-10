Conditionals
=============

Overview

--------

Conditionals offer a way for your code to make decisions. In the real world, an example of a conditional might be, if it is cold put on a sweater. A conditional in code looks like the following (see below). In the following code, the condition x == 5 is evaluated as either true or false. Note the double equals sign. The code x = 5 tells the program to set x to the value 5. The code x == 5 tells the program to compare the value of x and 5. If they are the same, the program returns true. If they are not the same, the program returns false.

.. code-block:: c
   
   if (x == 5) {                //Checks if this condition is true (i.e. does x equal 5). Note double equals sign
      Serial.println("true");  //If the condition is true than this line is executed.
   }
     

Schematic
---------

Set up the following circuit on your breadboard. MAKE SURE to use a long jump wire for the connection between pin 9 and ground. By moving one end of the wire between power (5V) and ground (leaving the other end in pin 9) you will be setting the input of pin 9 as HIGH and LOW respectively. This wire will essentially act as a crude button.

.. figure:: images/image101.png
   :alt: 

Code
----

#. In your  setup function, insert the following two lines to ensure that that pin 6 is an OUTPUT and pin 9 is an INPUT.

   .. code-block:: c

      pinMode(9, INPUT);        

      pinMode(6, OUTPUT):

#. Type the following code inside of the loop function. This code is set in the loop function because it needs to repeatedly check the value of pin 9. The following lines of code begining with "if" are referred to as a conditional statement. This is a code statement that evaluates a condition and runs code based on whether the condition is true or false.
   
   .. code-block:: c

      int x = digitalRead(9);    //Reads value of pin 9 and stores value in the variable x
   
      if (x == HIGH) {           //Checks if this condition is true (i.e. does x equal HIGH). Note double equals sign
         digitalWrite(6, HIGH);  //If the condition is true than this line is executed.
      }
      else {
         digitalWrite(6, LOW);   //If the condition is false than this line is executed.
      }

#. Compile and download your code.
#. Connect pin 9 to the power bus (HIGH). The LED should be lit.
#. Connect pin 9 to the ground bus (LOW). The LED should be off.

   Note that pin 9 and the wire are simply acting as crude button.

   TEACHER CHECK \_\_\_\_\_

#. What happens when pin 9 is not connected to ground or power? Move the wire around or touch it with your hand. A pin when not connected to power or ground is said to float. That means it is in an undefined state and can float between power and ground. IMPORTANT: Never leave a input pin hanging! Always attach it to power or ground.

#. Modify your code so that it reverses operation. The LED should be lit when pin 9 is connected to LOW and vise versa.

TEACHER CHECK \_\_\_\_\_
