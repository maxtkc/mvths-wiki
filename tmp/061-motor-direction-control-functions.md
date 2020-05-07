# Overview

Writing good functions for motor control are critical to effectively driving motors. A good motor control function can control both motor direction and speed. In this lesson, you will start with just controlling the direction of your motor.  If you need more information about functions, you can consult [concepts](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.45j551ci2de&sa=D&ust=1587613174178000).

### Exercise:

Write a function to control just the direction of one motor. The function can be called anything you like, but you may want to start with the following example.

void motor(int direction) {

//write your motor drive commands here

}

Write your motor code (within the motor function)  so that passing an argument of 1 will drive the motor forward and passing an argument of 2 will drive the motor in reverse. This way the following example commands can be used to call the function.

motor(1);  //to drive the motor forward

motor(2); //to drive the motors reverse

Using these examples as a starting point, write a complete program including a function to drive your motor. You program should drive the motor forward for 3 seconds and reverse for 3 seconds repeatedly.

TEACHER CHECK \_\_\_\_

### Exercise:

Modify your function so that instead of using the numbers 1 and 2 for forward and reverse, use the text forward and reverse. In order to do this, you will simply need to create defines for forward and reverse at the top of your code file.

TEACHER CHECK \_\_\_\_  
