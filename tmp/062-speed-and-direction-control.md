# Overview

This is the second part of a two part motor control lesson. In the previous lesson you wrote a function for controlling the direction of a motor. In this lesson you will add speed control to your function. Controlling the speed of your motor is typically done using PWM. If you are not familiar PWM consult the previous lesson on PWM.

# Basic Speed Control

The following is an example of a function that could be used for basic speed control assuming you are using pins 10 and 11 for controlling your motor module. Note that you will need to pass a second argument to control direction.

void motor\_speed(int speed\_value)

{

        analogWrite(10, speed\_value):

        digitalWrite(11, direction);

}

The following are three graphs showing different levels of speed control using the function above. Note that the analogWrite function is able to produce a PWM signal as shown below. When the AIN1 and AIN2 are opposite logic levels the motor moves forward. When they are the same logic level (both 0V) than the motor is in brake mode.

![](images/image88.png)

PWM motor control 50% duty cycle

![](images/image68.png)

PWM motor control 20% duty cycle

![](images/image33.png)

PWM motor control 80% duty cycle

### Exercise:

Using the function given above write a program to control the speed of your motor in one direction.

TEACHER CHECK \_\_\_\_

### Exercise:

Create a new function that is a duplicate of the motor function you created in the previous lesson for controlling motor direction. Change the name of this function to motor\_speed and use what you just learned about speed to control to enable your function to control both speed and direction of your motor. This will be challenging.

TEACHER CHECK \_\_\_\_  
