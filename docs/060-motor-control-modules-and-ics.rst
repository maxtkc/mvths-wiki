Motor Control Modules
=============================

Overview
--------

Since setting up bi-directional motor control using discrete components is difficult there are huge variety of motor control modules and integrated circuits. When selecting a motor control module to use the following are the most important criteria. 

**Current Rating:** This the amount of current that the motor driver can handle. For example, if you motor draws up to 2 Amps of current than you will need a motor driver that can handle more than 2 Amps of current. Generally, the more current a motor driver can handle the more expensive it is. Testing the amount of current a motor draws is as simple as connecting it to a power supply, setting the correct voltage and watching how much current it draws. Note that there is often a big difference between free running current and current under load. Free running current is the current draw when the motor is running without any load, i.e. nothing attached to the shaft. By adding a load to the motor, even just with your hand, you can see that it starts to draw more current. The maximum current a motor will draw is at stall or when the shaft is held so it can't move. This value is often quite high and can easily be 10 times the an average load current. Ideally, your motor module should be able to handle this current.

**Voltage Rating:** Voltage rating determine the minimum and maximum voltage for the motor module. Motors also are designed with a minimum and maximum voltage rating. It is important to make sure the range in which you intend to drive the motor fits within both the acceptable voltage range for the motor and the acceptable voltage range for the motor module.

**Circuit Protection:** Many motor modules include some sort of circuit protection. **Over current protection** is generally designed to protect the motor module from drawing too much current by shutting down. This means you could use a motor module that has a current rating below the stall current of the motor you are using if you can accept that the module will shut down when the motor stalls. **Thermal shutdown** is designed to shut down the module before it gets too hot. Motor modules can get very hot when they are operating at high current, **hot enough to burn your hand!** Too much heat can damage a module so some modules are designed to shut down before they get too hot.


