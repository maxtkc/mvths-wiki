Analog To Digital Conversion
============================

Overview
--------

The potentiometer you learned about in the previous section represents your first introduction to an analog signal. An analog signal is one 
that varies infinitely over time. As you saw with your multimeter, the potentiometer can be used to produce ANY voltage between zero and
five volts on your device. This is in contrast to the button which can only produce two distinct voltage levels, zero volts or five volts. 

Your microcontroller has two types of input pins, digital and analog. The digital pins are assigned D0 - D13 and the analog pins are assigned A0 - A5. 
While these pins have very different uses, it may help to understand them better if we consider then only different by degree. Digital pins can represent
voltages as one of only two states, either 0 (LOW) or 1 (HIGH) regardless of the voltage input. The datasheet for your device states that any 
voltage between 0V and 1.5V will be presented as a 0 (LOW) and any voltage between 3V and 5V will be repsented as a 1 (HIGH). Voltage values between 1.5V and 3V are 
indeterminate and may be represented as either 0 or 1. 

By comparison, an analog pin can read 1024 different states (0 - 1023) instead of just two, based on the voltage input. Essentially, the analog ports 
divide voltage input into much finer increments. The figure below shows how your microcontroller might read different input voltages on an analog pin. You can read more about analog pins `here <https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.kxihcorejof7>`__.

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

