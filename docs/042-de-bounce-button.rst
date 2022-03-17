De-Bounce Button
================

Overview
--------

Imagine pressing a momentary button like one on a keypad. The time during which it is pressed seems to be so short as to be irrelevant, yet microcontrollers process information at an incredibly fast rate, 16 million instructions per second in the case of the Arduino or one instruction every 62.5 nanoseconds (or .0000000625 seconds). By this measure our fingers are very slow.

The problem is that a lot of code can be executed during the time you are holding the button down, even you try to press it as quickly as possible. Sometimes, we don't want code to execute while a button is pressed, so we need a way to prevent this.

Button Pulse
------------

In order to write code to read a button press, you will need to understand the length of the average button press. The following shows how a button press might look on your oscilloscope.

.. figure:: images/image66.png
   :alt: 

Although the length of time a button is pressed may depend on may depend on many factors such as the device, or the mood of the user, it is possible to work out some useful guidelines for estimating the length of a button press.

Exercise
~~~~~~~~

#. Set your oscilloscope to the default set up.

#. Connect the output of a button circuit to your oscilloscope. Make sure to set up your button correctly using a resistor in the circuit.

#. Press the button and confirm that you see some movement on your oscilloscope screen.

#. Adjust the TIME/DIV on your oscilloscope so that you can see pulse like the one shown above when you press the button. 

   TEACHER CHECK ____

   In order to capture the button press more easily you may need to use the Trigger feature of your scope. Notice on the right side of your scope there is a section labeled trigger. In this section are a variety of controls that relate to the trigger as described below. 

   - **LEVEL**: This dial controls a small yellow arrow on the left side of your screen and cooresponds to the trigger level on your scope. The trigger level is the voltage level required for the scope to recognize a pulse. You generally want to set this level just below the voltage level of your pulse. So if you are looking for a pulse of 5 Volts then set the trigger level just below that. 
   - **Run/Stop**: This button allows you start and stop the trigger feature on your scope. In run, the scope is ready to accept signals. In stop, whatever is on the screen is frozen. This is useful for capturing continous waveforms that you want to read when a device is not running.
   - **MENU**: The menu button allows you to set various features of the trigger including the mode. Press the MENU button until you see the label Mode at the bottom right of the screen. Press the button next to the menu until the Mode changes from Auto to Normal. In the Normal Mode, the scope will wait for the trigger level to be tripped and then capture and hold just one pulse. 

#. Press the button and record the length of time for each press. In your notebook, record the fastest press and record what you feel is a "normal" press.       

   TEACHER CHECK \_\_\_\_

