Relational Operators
====================

Overview
--------

In this lesson you will learn to use the greater than and less than
logical operators. The greater than operator ">" checks if the value of a
variable is greater than a compared value and the less than operator "<"
checks if the value of a variable is less than a compared value.

x > 23 //If x is greater than 23 this returns true

x < 23 //If x is less than 23 this returns true

Conditionals
------------

In this lesson you will again need to use conditionals (ie. If and Then). Note you last
used a conditional in the lesson on Inputs. If you need a refresher, you can read more about
conditionals
`here <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.o11qq65yx4ek&sa=D&ust=1587613173938000>`__ in
concepts.

Exercise:
~~~~~~~~~

1. Set up your board with an LED and a potentiometer. Note the LED should be connected to a digital port and the
   potentiometer should be connected to an ADC port. Write a program
   that reads the value of the potentiometer and stores it in a variable. Add a conditional to check if the value
   from the potentiometer is greater than
   400. Add a line of code to turn on the LED if the the conditional is true.
   
2. Modify your code to turn off the LED if value of the potentiometer is less than 400. The LED should still turn on if the value is greater than 400.

TEACHER CHECK \_\_\_\_\_

3. Add two more LEDs to your board. Write a program that turns on the
   first LED when the value of the potentiometer is greater than 400, the second
   LED when the value of the potentiometer is greater than 600 and the third LED
   when the value of the potentiometer is greater than 800. Note that the order in which you check the value of
   the potentiometer in your code is important.
   
4. Modify your code so that the respective LEDs turn off when they are
   below the values given above. (i.e. the third LED turns on when the
   pot is greater than 800 and off when it is less than 800).

TEACHER CHECK \_\_\_\_\_
