Battery Control
===============

Overview
--------

Batteries offer a great way to power mobile robotic devices. Many are easily rechargeable and can provide large amounts of current for motors and other high current devices. There are many types of batteries defined by their chemistry. The common non-rechargable AAA or AA batteries are alkaline. Many AAA or AA rechargeable batteries are either nickel metal hydroxide (Ni-Mh) or nickel–cadmium (Ni-Cd). The batteries found in cell phones, laptops and electric cars are typically are either lithium-ion (Li-ion) or lithium-polymer (Li-Po). 

For the most part, we use Lithium Polymer (LiPo) batteries in our projects. The advantage of these sorts of batteries are that they can provide a large amount of power for their size and weight. They can be recharged quickly and can last much longer than other types of storage batteries. **DANGER:** The disadvantage is that if they are not managed carefully they can catch fire or even explode.

The following are important steps to take to ensure that your batteries and your circuit remain in working order

- **Balance Charge:** A LiPo battery should be charged to balance charge before being used in your device. The balance charge ensures that each cell in the battery pack is charged to the identical voltage level. Ask your teacher to demonstrate balance charge on the charging device.

- **Low Voltage:** It is important to make sure that the voltage in a battery never reaches below the danger threshold level. In order to ensure this does not happen, batteries should be checked every day using a LiPo tester. Ask your teacher to demonstrate testing.

- **Storage Charge:** Before returning a battery to storage it should be correctly discharged to a storage state selecting the Storage Charge state on the battery charger.

- **Connectors:** It is very important to only use polarized connectors with the LiPo batteries. These batteries are very powerful and can easily cause a fire and destroy your circuit in the following situations.

  - Short Circuit: If the two leads of the battery are allowed to touch each other, this causes a short circuit. At the very least this will cause a dangerous spark. It will also most likely damage the battery and cause a fire.

  - Reverse Polarity: If you mistaken reverse the leads on the battery and apply the positive lead of the battery to the ground on your circuit and the negative lead to power, you circuit and board will most likely be destroyed.

Challenge
~~~~~~~~~

Drive your motor control circuit using a single 7.2V (2 cell) LiPo battery. This challenge requires you to construct a connector from your battery to the breadboard, convert the 7.2V battery power to 5V for the logic circuits and pass the 7.2V to drive the motor. And make sure to get teacher checks for each step listed below. 

#. Create a battery connector with a polarized JST connector on one end mating with the JST connector on the battery and a two wire header on the other end that can plug into your breadboard. **IMPORTANT:** Make sure to use red and black wires with your connector and make sure they are polarized correctly! 

  TEACHER CHECK \_\_\_\_

#. Set up your breadboard (if you have not already done so) with 5 volt regulator to drive both the logic circuit and the motor controller.

  TEACHER CHECK \_\_\_\_

#. Tape your battery connector to your breadboard so that it will not easily fall off.

  TEACHER CHECK \_\_\_\_
  
#. Connect your lipo cable to your breadboard circuit.

TEACHER CHECK \_\_\_\_
