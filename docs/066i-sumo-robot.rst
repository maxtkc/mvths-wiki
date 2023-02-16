SUMO ROBOT CONTEST
======================

Overview
--------

In this project you will design and build a mini sumo robot for competition. Your robot must be designed according to the following specifications which are based on the international standards for the mini class of sumo robots. 

Requirements 
--------------

The following are a list of requirements for the design of your robot. 

- **Weight:** The total weight of your robot must not exceed 500 grams. 
- **Length and width:** The dimensions of your robot may be no more than 15 cm in length or width. A 15 cm square tube will be provided for testing the dimensions. Note: International standards are 10cm on each side.
- **Height:** There is no limit on height.
- **Logic Control:** A Metro Mini , Arduino Uno, or ATMega328P will be provided for logic control. Alternatively, you may choose to use another control platform. 
- **Circuit:** The final robot may not use a breadboard. All electronics may be soldered directly or part of a custom designed PCB.
- **Motor controller:** An MD17A motor controller module will be provided to drive the robots motors. Alternatives are allowed.
- **Motors:** The robot will use standard DC plastic geared motors. You will have a choice between two gear ratios either 120:1 or 200:1. Alternative: You may use motors after consulting with a teacher.
- **Wheels:** No wheels will be provided. These can be custom made using any material.
- **Tires:** O-rings in 2 inch or 3 inch diameters will be provided for use as tires. Alternatively, you may custom cast your own tires.
- **Battery:** The robot will be use a 7.2 Volt LiPo battery which has a capacity of 1000mAh. The robot must include a secure holder for the battery.
- **Line sensors:** Two QTR-1A photo-reflective sensors will be provided for tracking lines. Additional sensors and alternative sensors may be used. 
- **Object sensors:** One VL53L0X sensor will be provided for detecting other robots. Additional sensors and alternative sensors may be used. 
- **Start Button:** The robot must use a momentary soft latching push button for the purpose of starting the robot during a competition. This button will be provided. The robot must also include a three second delay before it starts. 
- **Cost:** The total cost for additional parts and construction of the robot must not exceed $40. Details are provided below.

Cost
----

The cost of your project will be the sum of the cost of the materials you use to create all of your parts and the cost of any additional parts you use or purchase for your project. 

Material Costs
^^^^^^^^^^^^^^
Materials include those in your final robot as well as those you use to develop your robot. For example, if you build a wheel and do not use it, the cost of materials for that wheel will be included in your total budget. Below is a list of costs for a majority of materials. Note that for the first four items there is a 30% markup due to material waste. 

.. list-table:: Material Costs
   :widths: 25 25 25
   :header-rows: 1

   * - Material
     - Cost
     - Units
   * - Cardboard
     - Free
     - square inch
   * - Acrylic (1/8)
     - .16
     - square inch
   * - Acrylic (1/4)
     - .25
     - square inch
   * - Acrylic (1/2)
     - .60
     - square inch
   * - Plywood (1/8 inch)
     - .12
     - square inch
   * - Plywood (1/4 inch)
     - .14
     - square inch
   * - PLA (Fusion3)
     - .70
     - cubic inch
   * - PLA (Stratasys)
     - 5.00
     - cubic inch
   * - Resin (Formlabs)
     - 3.50
     - cubic inch
   * - Cooper board (PCB)
     - .80
     - board (4"x5")

Steps
--------

#. **Motor Control:** Build a breadboard circuit using an Arduino-style board i.e. Uno or MetroMini that able to control the speed and direction of two motors. You will use the MD17A from Pololu for motor control. One MD17A is able to control two motors. At this point, do not worry about which of the gear ratios (120:1 or 200:1) you are using. You can easily swap out motors at any time. A good test of completion is being able to write code to drive each motor independently forward and reverse for 3 seconds. 

#. **Line Sensor:** Add a QTR-1A photo-reflective sensor to your circuit. Add an LED to your circuit. Write code to turn on the LED when the QTR-1A senses reflection (a white line). Now write code to control one motor based on the feedback from the QTR-1A. Add a second QTR-1A to your circuit and confirm that this one can control a motor as well. While the LEDs might not seem necessary to your final design, they can provide invaluable feedback that your sensors are working correctly, when trying to troubleshoot a complex robot.

#. **Battery Power:** Add a 7.2 Volt LiPo battery to power your circuit. These batteries come with red polarized JST connectors. You will need to create a cable with a matching polarized JST connector at one end (for the battery) and a simple two wire connector at the other end (for the breadboard). These connectors must be crimped with red and black wires that MUST correspond to power and ground respectively. Be VERY careful when you set up this connector to ensure that the red and black leads or oriented correctly. You must tape the breadboard end to your breadboard to ensure that this end is not accidently reversed. If it is reversed, even for a millisecond, your whole circuit goes bye, bye. IMPORTANT: Before connecting your battery, show this circuit to your teacher.

#. **Wheels:** Design a wheel that corresponds to the 2-inch or 3-inch rubber o-ring provided for tires. This wheel must be designed to mate securely with the motor shaft. The wheel must also have a groove to hold the tire securely. If your tire (or wheel) falls off during competition, your will not be a happy person. You must include a model of the o-ring in your design. Print one wheel and test. Note: This print will be charged against your account. If the print is successful, create a second wheel.

#. **Basic Frame:** Design a very basic but complete robot. Do not worry about size restrictions or tactical design. This is simply a testing platform to make sure everything works properly and to begin to hone your final design. This frame should be built from cardboard as much as possible. The frame should be able to hold the motors, breadboard, battery, sensors and a castor (see below). This design MUST include ALL parts of your robot design including those parts you are not building, i.e. motors, battery, sensors and breadboard. 

#. **Castor:** This castor will form the third wheel for your robot. The two wheels attached to the motor will drive and turn the robot. The caster prevents the robot from falling over. It should be designed to hold a small steel ball bearing (removed from cars in auto tech). The bearing should be held in place by the caster but should also be able to roll freely. Below are some guidelines for making a good caster. This design will be discussed in class.

   The caster should:
      - cover at least 200 degrees but no more than 300 degrees total of the ball bearing. 
      - have a shell thickness of at least .06”.
      - have an inner diameter .03” larger than the diameter of your ball bearing.
      - have at least three expansion cuts of at least 60 degree arc.
      - include a brass insert for mounting to robot frame. 
      
#. **Testing:** A fully tested robot should be able to remain in the sumo ring for 45 seconds, the average time of a sumo match.

Final Steps
-----------

Once your robot is fully tested, you should begin to work on the final construction steps for your robot. These following steps are not provided in any specific order.

- Adding one or two VL53L0X sensors to detect the presence of another robot. 
- Converting your breadboard circuit to a PCB.
- Adding a soft power switch to start your robot. 
- Finalizing the frame design for your robot.







