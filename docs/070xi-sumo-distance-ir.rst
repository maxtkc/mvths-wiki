Sumo Distance Sensor TF
======================

Overview
--------

In this lesson, you will learn how to setup and use Sharp 2Y0A21F infrared sensor to measure the distance between your robot and another robot. The Sharp 2Y0A21F is a rangefinder infrared sensor that sends out a beam of infrared light and then detects light reflected from the object. It uses the angle of reflection to determine the distance. 

The device is powered bu 5V and a produces and analog that correlates inversely to distance. A closer object produces a higher voltage. The sensor can detect objects ditances from 10cm to 80cm.  

.. figure:: images/irsensor.jpg
   :alt: 

Set up
------

#. Connect the red lead from the sensor to 5V.

#. Connect the black lead from the sensor to ground.

#. Connect the yellow lead from the sensor to one of your analog inputs. 

#. Write a program to read the raw value from the sensor and display this value in your terminal window.
