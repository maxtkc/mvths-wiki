Button Software
---------------

The following are two basic strategies for using a button to control the states within your microcontroller.

-  **Direct state control**, the state of the button equals the state of the device. For example, a direct state control of an LED would turn the LED on when the button is pressed and off when the button is not pressed.
-  **Toggle state control**, the button can transition a device between two states. For example in toggle state control of an LED, the LED would change its state (on or off) after each button press.

Exercise
~~~~~~~~

1. Construct a circuit and write a program to demonstrate direct control using a button and an LED. The LED should remain on as long as the button is pressed and turn off when the button is not pressed.

TEACHER CHECK \_\_\_\_

2. Using a single button demonstrate toggle control over one LED. There are two ways to solve this problem. One is create a new variable to store the state of the button press. The second is to toggle the state of the LED. You can find information on toggling an LED on line.

NOTE: If your circuit is not reliable (i.e. not consistently changing states), you might need a delay after your button press that is longer than the average time of a button press. This will ensure that your code is not continually checking the state of a button while it is pressed.

4. TEACHER CHECK \_\_\_\_
