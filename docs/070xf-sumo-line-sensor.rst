STEP SEVEN: Line Sensor Setup
======================

Overview
--------

In this lesson, you will learn how to use a QTR-MD-01A Reflectance Sensor to distinguish between light and dark surfaces. Specifically, this sensor will be used to detect the white line on the outside of the sumo ring.

.. image:: images/sumoring.PNG
      :width: 400px

The QTR-MD-01A sensor (shown below) includes a photo emitter and sensor pair as well as well as other necessary components. The schematic for the sensor is shown below as well. On the left side of the schematic is the IR emitter which sends out infrared light. On the right of the schematic is the phototransistor which senses infrared light. The voltage at the OUT pin varies depending on how much infrared light is reflected from the IR emitter. You can check out the `product page <https://www.pololu.com/product/2458>`__  for additional information. 

.. image:: images/linesensor.PNG
      :width: 400px

.. image:: images/linesensorschematic.PNG
      :width: 400px
      
Specifications
-------
The sensor has three pins for power (labeled VCC), ground (labeled GND) and signal (labeled OUT). The sensor operates from 2.9 V to 5.5 V. The output signal is analog and should be connected to an analog port. While the sensor can detect objects from 30mm, it works optimally at 5mm.

Set up
--------
#. If the three control pins (VCC, GND, OUT) are not soldered, you can solder either three wires to the sensor or a right angle header. 
#. Connect the sensor to your breadboard, connecting VCC to the 5V bus and GND to ground.

Testing
--------
Using a multimeter, test that your sensor is working correctly.

#. Connect the signal lead (OUT) of the sensor to the input lead of your multimeter and the ground lead to ground. I recommend using the alligator leads for this.
#. Set the meter to measure voltage. 
#. Power your circuit with either a USB cable or your battery supply.
#. Place a light or white object infront of your sensor and record the voltage.
#. Place a dark or black object infront of your sensor and record the voltage. 
#. Is the voltage higher or lower with a white object infront of the sensor?
#. Does it matter how far away the objects are from the sensor?
#. Repeat your tests at approximately 5mm which is the ideal sensing range for the sensor. 




#. Record the highest and lowest voltage values in your notebook. Include correct units.

   - Lowest voltage value: ________
   
   - Highest voltage value: ________
   
#. One of the problems with testing the reflectance sensor is that it responds not only to the IR light from the emitter, but to stray IR light all over the room. Sunlight and incandescent lights emit IR light along with other wavelengths of the light spectrum. This stray light can "fool" your sensor. Record the value of the sesnor facing a window and facing a reflective surface (i.e. reflecting light from the room).

   - Facing window: __________
   
   - Facing reflective surface: ________

#. As noted above, the value on the signal lead (OUT) is proportional to how much light is reflected from the emitter to the receiver. Using various reflective and non-reflective material, determine if the value (voltage) increases or decreases based on reflectivity. Essentially, the white line is meant to reflect IR light back into the sensor and the black ring is meant to not reflect IR light. You need to determine if you should see a higher voltage when the sensor is over while or when the sensor is over black. Record your findings in your notebook.

   - White surface: _________________
   
   - Black surface: _________________
   


