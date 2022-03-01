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

PCB 
Start button
Distance sensor









 TEACHER CHECK ____

Build Prototype
Now that you have all of your electronics working on a breadboard, you should design a working prototype of your robot in 2
Construct PCB
Design and construct a circuit board that holds the entire circuit you prototyped in the lessons above. In order to design and construct the board you will need to use Eagle CAD and our OtherMill CNC mill. If you are not familiar with Eagle CAD than you will need to follow the tutorial found here. 

Frame
The frame should be designed from one or more 2 dimensional parts that can be laser cut. Initially, you will use cardboard for your design. Once the design is constructed and demonstrated, you may use either plastic or wood. The frame must include:

Holes for mounting the your circuit board
Holes for mounting the motor brackets
A hole for mounting the castor
A hole for mounting the momentary switch
A method for holding the battery
A method for holding the line sensors a specific distance above the table
A method for holding one or two distance sensors

 TEACHER CHECK ____
Create Assembly
Collect of the robot parts into a single assembly. Put the parts together to form a complete robot. Ensure that the base frame is level when both wheels and caster are placed on a surface. If not, adjust the height of the castor. Ensure that the robot is balanced between the castor and wheels, so that it does not fall over when accelerating.
Build Robot Base
Cut and print all parts and assemble robot. Do not forget to secure threaded brass insert in caster. Make sure of the following:

Do motor mount holes line up with holes on frame?
Do wheels fit snug on motor shaft?
Do tires fit snug on wheels?
Does bearing fit lose and secure in castor?
Does switch fit in hole on frame?
Does breadboard and battery fit snug on frame?
Software and Testing
In order to drive your robot you will need to write software to control the motors. Complete the following drive tests.

Basic Drive
Write a program to drive your motors forward for one second and then reverse for two seconds. You should include a small delay of half a second between the forward and reverse motors. This pattern should repeat indefinitely. Demonstrate the motion of your motors with your robot “on blocks” so that the motors are not in contact with a surface.

Initial Pattern
Write a program to drive the robot forward for 18 inches, turn around completely (180 degrees) and drive back to the starting position.  

Function Drive
Write programs to complete the following two patterns. You drive software must include a function for driving each motor. The length of each line is 16 inches.





Hi Mr. Christy
