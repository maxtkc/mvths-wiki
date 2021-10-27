De-Bounce Button
================

Overview
--------

Imagine pressing a momentary button like one on a keypad. The time during which it is pressed seems to be so short as to be irrelevant, yet microcontrollers process information at an incredibly fast rate, 16 million instructions per second in the case of the Arduino or one instruction every 62.5 nanoseconds (or .0000000625 seconds). By this measure our fingers are very slow.

Button Pulse
------------

In order to write code to read a button press, you will need to understand the length of the average button press. The following shows how a button press might look on your oscilloscope.

.. figure:: images/image66.png
   :alt: 

Although the length of time a button is pressed may depend on may depend on many factors such as the device, or the mood of the user, it is possible to work out some useful parameters for button press length using your oscilloscope.

Exercise
~~~~~~~~

Connect the output of a button circuit to your oscilloscope. Adjust the TIME/DIV on your oscilloscope so that you can see pulse like the one shown above when you press the button. 

In order to capture the button press more easily you will need to use the Trigger feature of your scope. Notice on the right side of your scope there is a section labeled trigger. In this section are a variety of controls that relate to the trigger. 

- **LEVEL**: This dial controls a small yellow arrow on the left side of your screen and cooresponds to the trigger level on your scope. The trigger level is the voltage level required for the scope to recognize a pulse. You generally want to set this level just below the voltage level of your pulse. So if you are looking for a pulse of 5 Volts then set the trigger level just below that. 
- **Run/Stop**: This button allows you start and stop the trigger feature on your scope. In run, the scope is ready to accept signals. In stop, whatever is on the screen is frozen. This is useful for capturing continous waveforms that you want to read when a device is not running.
- **MENU**: The menu button allows you to set various features of the trigger including the mode. Press the MENU button until you see the label Mode at the bottom right of the screen. Press the button next to the menu until the Mode changes from Auto to Normal. In the Normal Mode, the scope will wait for the trigger level to be tripped and then capture and hold just one pulse. 

Pressing the button, record the following in your notebook.

        Length of shortest button press:         

        Length of average button press:        

TEACHER CHECK \_\_\_\_

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
