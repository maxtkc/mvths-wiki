# Overview

In this lesson you will combine your knowledge of pulse width modulation (PWM) and motor control to control the speed of your motor. PWM is the most common method used to control DC motors such as those in electric drills or electric cars.

# PWM

In the lesson above, you controlled the motor by turning it full ON or full OFF. Using PWM, you can create a control signal that is both ON and OFF. The proportion of ON time versus OFF time determines the speed of the motor. This proportion is known as the duty cycle (for a review of duty cycle see above). When the duty cycle is lower (less ON time), the motor will run slower. When the duty cycle is higher (more ON time), the motor will run faster.

Using the same circuit you constructed in the previous lesson. Write a new program to drive your motor using PWM with a 50 percent duty cycle. If need a review you can refer to the lesson (PWM) [analogwrite](#h.pqdu75uhcuwd). All of your code should be in the setup function.

TEACHER CHECK \_\_\_\_
