STEP THREE: Software Control
=============================

Overview
--------
In this lesson, you will turn a motor on and off and control its direction using code. 

Set Up
--------
Instead of conneting pins AIN2 and AIN1 directly to power or ground, connect each one to a different digital pin on your Metro Mini. This will allow you to control the motor in software instead of moving the pins between power and ground.

The Code
-------
Write a few programs to control your motors.

#. Write a program to drive one motor clockwise for three seconds and then stop. Don't forget to set the pinMode for each pin. Are these going to be inputs or outputs? You should know this.
#. Write a program to dive one motor clockwise for three seconds and then counter clockwise for three seconds, repeating.
#. Modify the above code so that the motor stops for two seconds between each time it changes direction.

Pin Defines
-------
Use defines instead of integers to identify the pins you are using to control your motor. If you need to, you can revisit the lesson on `defines. <https://mvths-wiki.readthedocs.io/en/latest/042cc-defines.html>`_

#. Replace the integer values you are using for your two pins with defines. An example might be MT!A and MT1B but make sure they mean something to you.
#. Write a program to drive your motor for 2 seconds counterclockwise, 2 seconds stop and 3 seconds clockwise. This time with defines.
