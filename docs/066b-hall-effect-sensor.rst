Hall Effect Sensor
==================

Overview
--------

Hall effect sensors are designed to detect the presence of a magnetic
field. They are used in a variety of applications included detecting if
a door is open or closed, and counting rotations of a motor. The hall
effect sensor you will be using is the US5881. You can find a datasheet
for this device
`here <https://www.google.com/url?q=https://cdn-shop.adafruit.com/datasheets/US5881_rev007.pdf&sa=D&ust=1587613173981000>`__.


.. figure:: images/image92.png
   :alt: 

Exercise:

1. Collect one US5881 from the bins. The device has U58 printed on the
   front of the component.
2. Using the datasheet as a reference, record the Max. and Min. supply voltage for this device in your notebook. These
   specifications can be found on page 4 of the datasheet.

3. Draw diagram (picture) of the US5881 in your notebook. A box with three lines for pins will do. Write the function for each of the three pins. This
   information can be found on page 3 of the datasheet. IMPORTANT: THIS IS A UA PACKAGE. THERE ARE TWO TYPES OF PACKAGES (UA AND
   SE) SHOWN ON THE DATASHEET. Make sure to write down the pin functions for the UA package not the SE package. Note that VDD or supply is the power pin
   for this device.

TEACHER CHECK \_\_\_\_

4. On page 7 of the datasheet you will find the Typical Three-wire
   Application Circuit (12.1) Set up this circuit as described. 
   
   #. Pin VDD should be connected to your power supply. 
   #. Pin VSS (or ground) should be connected to your ground. 
   #. Pin OUT should be connected to a digital pin on your microcontroller with a pull-up resistor. That is a 10k resistor connecting the output to power.
   
   Note:
   You do not need to include either capacitor for testing purposes.
   They are only recommended for a commercial application. Make sure to
   always remove power from your circuit when adding a device.

TEACHER CHECK \_\_\_\_

5. Set up a multimeter to measure the voltage output of the hall effect sensor for when it is near a magnet is near to it. You may need a
   paperclip to easily hold the magnet near the hall effect sensor. Record your readings below. I also strongly suggest using alligator 
   clips to hold your meter leads. Write down your results in your notebook.

6. Record the distance at which the sensor detects the magnet and write this number in your notebook.



TEACHER CHECK \_\_\_\_
