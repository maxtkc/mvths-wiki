For Loops
=========================

Overview
--------

In this lesson, you will create for loops. For loops are one of the key features of any programming language. They allow you to increment or decrement a variable over
a precise range of numbers. The following is a basic a example of for loop that prints the numbers 0 to 9 in your terminal window. There are three parts to the 
for loop. The first part sets the inital value of the variable "x = 0". The second part sets the final value of the variable "x < 10". More specifically, this line
is a conditional. It says keep running the loop while "x < 10". As soon as this statement is no longer true, the loop stops running. The last part tells the loop to 
add one to the variable each time through the loop.

.. code-block:: C
  
  for (x = 0; x < 10; x = x + 1) {
    Serial.println(x);
    delay(10);
  }
  
  
Exercise:
~~~~~~~~~

1. Copy the above code into your setup() function, NOT loop(). 
2. Include in your code file everything else you need to run this code.
3. Display the results in your terminal window.

TEACHER CHECK \_\_\_\_\_

4. Modify your code so that it starts counting from a differnt initial value.
5. Modify your code so that it counts to a different final value.
6. Mofify your code so that it counts by a different increment (not just one).

TEACHER CHECK \_\_\_\_\_

7. Modify your code so that it counts down by 1 from 94.

TEACHER CHECK \_\_\_\_\_

8. Place your for loop code into your loop() function and note the difference.
