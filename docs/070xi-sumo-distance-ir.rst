Sumo Distance Sensor TF
======================

Overview
--------

In this lesson, you will learn how to setup and use a VL53L0X time of flight (TOF) sensor to measure distance to determine the distance between your robot and another robot. The VL53L0X uses the elpase time it takes photons to travel between to points to measure distances from 3cm to 100cm. The device is 5V compatible on pin VIN and communciates via I2C on pins SDA and SCL.

.. figure:: images/image78.png
   :alt: 

Set up
------

#. Connect your VL53L0X to an Arduino Uno or Metro Mini using I2C. You can connect VIN to 5V. If you have not used an I2C device before, you can review the lesson on I2C devices. Note t
