Sumo Distance Sensor TF
======================

Overview
--------

In this lesson, you will learn how to setup and use a VL53L0X time of flight (TOF) sensor to measure distance to determine the distance between your robot and another robot. The VL53L0X uses the elpase time it takes photons to travel between to points to measure distances from 3cm to 100cm. The device is 5V compatible on pin VIN and communciates via I2C on pins SDA and SCL.

.. figure:: images/image78.png
   :alt: 

Set up
------

#. Connect your VL53L0X to an Arduino Uno or Metro Mini using I2C. You can connect VIN to 5V. If you have not used an I2C device before, you can review the lesson on I2C devices. Note that you will only need four connections, VIN, GND, SDA, and SCL.

#. Check if the Adafruit_VL53L0X library is installed in your IDE. If not, install this library from Library Manager.

#. Open the vl53l0x project from Examples/Adafruit_VL53L0X.

#. Upload the example code to your board.

#. Open your terminal window.

#. Note that the code runs at 115200 so you will need to set this baud
   rate in the terminal window. You should see:
.. code-block:: c

   Adafruit VL53L0X test

   VL53L0X API Simple Ranging example

   ...and then a set of distance readings in mm.

Using the Sensor with your Sumobot
------------------------------------

The following is example code that can be used to detect if an object is between 50mm and 100mm from the sensor.

.. code-block:: c

   // This is the library required for the sensor
   #include "Adafruit_VL53L0X.h"

   // Create an object for the sensor
   Adafruit_VL53L0X lox = Adafruit_VL53L0X();

   int dist;
   
   void setup() {                
       Serial.begin(115200);
       
       lox.begin();  // Initialize the sensor
   }
   
   void loop() {
       VL53L0_RangingMeasurementData_t measure; // Take a measurement
    
       lox.rangingTest(&measure, false);
    
       dist = measure.RangeMilliMeter;
    
       if ((dist < 100) && (dist > 50))
    
       Serial.print("In the zone: ");
    
       Serial.println(dist);
       delay(100);
    }

   
