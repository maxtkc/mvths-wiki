Motor Defines
=================================

Overview
--------

As you learned in an earlier lesson, defines make your code much easier to read. Given the potential complexity of your sumo code, I strongly recommend beginning with defines. 

Exercise:
~~~~~~~~~

Write a function to control just the direction of one motor. The function can be called anything you like, but you should use a name that best indicates the purpose of the function. The following is just one example.

.. code::

   void motor(int direction) {

      //write your motor drive commands here

   }

Write your motor code (within the motor function)  so that passing an argument of 1 will drive the motor forward and passing an argument of 2 will drive the motor in reverse. This way the following example commands can be used to call the function.
