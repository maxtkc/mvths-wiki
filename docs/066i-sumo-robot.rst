SUMO ROBOT CONTEST
======================

Overview
--------

In this project you will design and build a mini sumo robot for competition. Your robot must be designed according the following specifications which conform to the international standards for the mini class of sumo robots. The cost of construction of the robot must not exceed $40. A description of how to calculate costs is provide below.

Specifications 
--------------

- **Weight:** The total weight of your robot must not exceed 500 grams. 
- **Length and width:** The dimensions of your robot may be no more than 10cm in length or width. A 10cm square tube will be provided for testing the dimensions. 
- **Height:** There is no limit on height.
- **Programmable controller:** The robot will use a ATMega328 microcontroller for logic control.
- **Circuit:** The final robot will use a custom designed PCB for the all electronics.
- **Motor controller:** The MD17A motor controller module will be used to drive the robots motors.
- **Motors:** The robot will use standard DC plastic geared motors. You will have a choice between two gear ratios either 120:1 or 200:1. Alternative: You may use motors after consulting with a teacher.
- **Wheels:** The wheels may be custom designed. You will have a choice of two tire sizes either 2 inch or 3 inch. Alternatively: You may cast your own tires of any size.
- **Battery:** The robot will be use a 7.2 Volt LiPo battery which has a capacity of 1000mAh. The robot must include a secure holder for the battery.
- **Line sensors:** The robot will use the QTR-1A photo-reflective sensors for tracking lines and may include up to three photo reflective sensors. 
- **Object sensors:** The robot will use the VL53L0X sensor for detecting other robots. The VL53L0X is a time of flight sensor and the robot may include up to two of these sensors. 
- **Switch:** The robot will use a momentary soft latching push button for the purpose of starting the robot during a competition.

Cost
----
The total cost of construction of your robot must not exceed $40. This includes the cost of all consumables used in the construction, testing or final design. A consumable is any part or material that no longer has value after it has been used. For example, this includes any plastic or wood that you cut or print for your project. This also includes any part that is broken or any part that has been directly soldered to a board. This does not include parts that can be reused after final construction of your robot, for example, sensors that can be removed from your project. This also does not include any cardboard. This does include plastic or wood that is used for testing or is replaced as your design evolves. 

.. list-table:: Material Costs
   :widths: 25 25 25
   :header-rows: 1

   * - Material
     - Cost
     - Units
   * - Cardboard
     - Free
     - square inch
   * - Acrylic
     - .30
     - square inch
   * - Wood
     - .30
     - square inch
   * - PLA (Fusion)
     - .30
     - cubic inch
   * - PLA (Stratasys)
     - .30
     - cubic inch
   * - Resin (Formlabs)
     - .30
     - cubic inch
   * - Cooper board (PCB)
     - 1.00
     - board

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







