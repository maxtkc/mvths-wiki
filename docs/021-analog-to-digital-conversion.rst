Analog To Digital Conversion
============================

Overview
--------

In addition to the digital pins on your microcontroller number D0 through D13 there are also six analog pins assigned A0 - A5. These analog pins are desgined to read analog signals and convert them to a digital format that the microcontroller can use. 

Up till now all of the inputs used with your microcontroller have been digital. A digital input is one that has fixed states. A button, for example, only has two states, either pressed or not pressed. Electrically these states are represented as voltages, 5V or 0V. The potentiometer you learned about in the previous section (but have not yet used as an input) represents your first introduction to an analog signal. An analog signal is one that varies infinitely over time. As you saw with your multimeter, the potentiometer can be used to produce ANY voltage between 0V and 5V.

Your microcontroller is an inherently digital device so in order for it to read a signal from a potentiometer, it must be able to convert this analog signal to a digital signal using one of the six analog ports. Since the analog ports on the microcontroller you are using are 10-bit they convert any analog signal (between 0V and 5V) to one of 1024 different states (0 - 1023).  


.. figure:: images/image109.png
   :alt: 

Exercise
~~~~~~~~

1. If you connected a potentiometer to a digital pin on your microcontroller 
   what would the microtroller read when you turned the dial of the potentiometer? Write your answer in your notebook.
   
2. If you connected a button to an analog pin on your microcontroller what would your microcontroller read when you
   pressed the button? Write your answer in your notebook.
   
3. If you connected a potentiometer to an analog pin on your microcontroller and turned the dial half way, approximately what
   value do you think you would read in your microcontroller? Write your answer in your notebook.
  
4. TEACHER CHECK \_\_\_\_

Code
----

In order to use the analog to digital converter (ADC) on your Metro Mini
you will need to use the following command. Note that this function will return the values 0 to 1023 depending on the voltage it reads at the analog pin.

.. figure:: images/image99.png
   :alt: 

Exercise
~~~~~~~~

1. **Reading a Potentiometer**: Add a potentiometer to your board if you do not already have one set up. See the 
   previous section for how to set up a potentiometer. Connect the output of your potentiometers to an ADC port on
   your microcontroller. Remember there are five ADC ports (A0 - A5). 
   
2. Use the command above to read a value from this port. Make sure to place this line in your code where
   it will be read continously. 
   
3. Display the value from your potentiometer in a column on your serial monitor.  Note this value is stored 
   in the variable x. You will need a serial command to print the value of the variable in your serial monitor. The
   value you see should range from 0 to 1023 proportional to how you turn the potentiometer.

TEACHER CHECK \_\_\_\_

