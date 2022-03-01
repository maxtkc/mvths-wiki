SUMO ROBOT CONTEST
======================

Overview
--------

In this project you will design and build a mini sumo robot for competition. Your robot must be designed according the following specifications which conform to the international standards for the mini class of sumo robots. The cost of construction of the robot must not exceed $40. A description of how to calculate costs is provide below.

Specifications 
--------------

**Weight:** The total weight of your robot must not exceed 500 grams. 
**Length and width:** The dimensions of your robot may be no more than 10cm in length or width. A 10cm square tube will be provided for testing the dimensions. 
Height: There is no limit on height.
Programmable controller: The robot will use a ATMega328 microcontroller for logic control.
Circuit: The final robot will use a custom designed PCB for the all electronics.
Motor controller: The MD17A motor controller module will be used to drive the robots motors.
Motors: The robot will use standard DC plastic geared motors. You will have a choice between two gear ratios either 120:1 or 200:1. Alternative: You may use motors after consulting with a teacher.
Wheels: The wheels will be custom designed and 3D printed. You will have a choice of two tire sizes either 2 inch or 3 inch. Alternative: You may cast your own tires of any size.
Battery: The robot will be use a 7.2 Volt LiPo battery which has a capacity of 1000mAh. The robot must include a secure holder for the battery.
Line sensors: The robot will use the QTR-1A photo-reflective sensors for tracking lines and may include up to three photo reflective sensors. 
Object sensors: The robot will use the VL53L0X sensor for detecting other robots. The VL53L0X is a time of flight sensor and the robot may include up to two of these sensors. 
Switch: The robot will use a momentary soft latching push button for the purpose of starting the robot during a competition.

Cost
The total cost of construction of your robot must not exceed $40. This includes the cost of all consumables used in the construction, testing or final design. A consumable is any part or material that no longer has value after it has been used. For example, this includes any plastic or wood that you cut or print for your project. This also includes any part that is broken or any part that has been directly soldered to a board. This does not include parts that can be reused after final construction of your robot, for example, sensors that can be removed from your project. This also does not include any cardboard. This does include plastic or wood that is used for testing or is replaced as your design evolves. 

	Charge			No Charge
	Acrylic sheet			Cardboard
	3D printed parts		Chipboard
	Wood				Testing wheels
Crude Bot
In this initial phase of design, you will construct a basic robotic testing platform. The goal of this exercise is to give you a simple, low cost, easy to modify platform for testing your code, motor drivers and sensors. The basic platform should be a 
 
Construct Circuit
Overview
Design and construct a complete electronic circuit on a breadboard for controlling your robot’s motors and sensors. 
Logic control
Construct a microcontroller-based (ATMega328) circuit on a breadboard. Confirm that the circuit is setup correctly by downloading some sample code to it. 

 TEACHER CHECK ____
Power cable  
In order to create a mobile robot, you must use a battery for your power supply. Using a battery frees your robot from the USB cable that is typically used to power your circuits and provides enough current and voltage to drive your two motors.

Construct a cable to connect your battery (see Lessons) to your breadboard. The cable will need to have a two pin connector on one end and a polarized male JST connector that is compatible with the battery connector on the other. Tape your battery connector to your breadboard. This is so you do not accidentally reverse the polarity to your circuit and your circuit     goes boom. 
 TEACHER CHECK ____
Start button
In order to make sure all robots start at the same time and to safely use the lipo batteries, you will need to install a start button on your robot. This will consist of a simple momentary soft latching switch (see Lessons). 

Challenge
Connect the switch to your circuit board. Demonstrate that it controls power to your             .board. 
 TEACHER CHECK ____
Motor control
Construct a motor control circuit using the MD17A that can be programmed to control the speed and direction of two motors. Design the circuit using the components listed above. Do not worry about which version of the motor you use. You can change motors at any time in the project. If you need help with the circuit you can refer to the guide in Lessons for the MD17A. 

Challenge:
Write a program to drive both motors forward for two seconds, then backwards for two seconds, then in opposite directions for two seconds. Your code should include motor control functions as described in   the Lessons Guide. 
 TEACHER CHECK ____
Line sensor
Add two QTR-1A photo-reflective sensors to your circuit and modify your code so that your motors respond to feedback from two line sensors. If you need a reminder on how to use the QTR-1A, refer to the guide in Lessons for this sensor. 

You may want to consider adding two LEDs to your circuit to indicate when your sensor has detected a line. This could be useful for troubling shooting.

Challenge: 
Write a program that changes the direction of both motors when either of the photo-reflective sensors detects a white line.

 TEACHER CHECK ____
Distance sensor
Add a single VL53L0X distance sensor to your circuit. This is a time of flight sensor that will be used to detect if another robot is in its vicinity. You may use up to two of these sensors on your robot.

Challenge
Modify your code so that both motors change direction when an object is six inches or closer to your robot.

 TEACHER CHECK ____

Build Prototype
In this next step, you will build a working prototype of your model. This model should be designed with plastic printed wheels and caster. The remainder should be designed in cardboard. 

Create Models
Before you print or cut any of the parts of your robot, you must design the entire robot using CAD and create the robot as a complete assembly. The first step will be create models of all of the existing parts you will using in your project. Then construct the new parts and then construct an assembly.

In this first exercise, you will create models in CAD of all the existing parts that you are going to use in your project. Remember to create functional models of all your parts. This means including only details of the part that are necessary for the project. Make sure to save all of your models on Github. You will use these models again.

Battery
In this project you will be using a small 7.4 Volt (2 cell) LiPo battery. The basic shape of the battery pack can also be modeled as a rectangular box. You should include the wires as well as the connector.
Battery Connector
Create a model of the battery cable connector that you constructed in the initial challenge of this project.

Switch
You will be mounting a small momentary switch to control the power to your robot. This will need to be modeled fairly closely to the original with the mounting holes.
Motor
You will be using a standard plastic geared motor for this project. You will need to model the general shape of the motor along with the mounting holes correctly placed.
Motor mount
The motor mount is a fairly simple device and should be modeled fairly accurately.
Tire
Make a model of both the large and small tire options for this project.
Bearing
Make a model of the bearing that will be used for the caster in this project.
Circuit Board
You should be able to create a model of your circuit board from with Eagle.

 TEACHER CHECK ____
Design Parts
Design the following parts in CAD. As you design parts, be sure to keep in mind the overall constraints of weight and size for your robotic platform.
Wheels
Design a wheel that can hold either the large or small tire (as defined above). When choosing the exact diameter, it is best to err on the side of being too large versus too small. If the tire is too large as compared with the wheel it is more likely to slip off during operation. The tire should fit into a strong groove around the wheel so as to ensure that it does not fall off during operation. The center of the wheel must be designed to press fit onto the plastic motor (as described above). Keep in mind the overall weight requirement of your robot when designing your wheel. Note that your wheel will be printed using the 3D printer.

 TEACHER CHECK ____
Caster
Design a caster that hold a bearing (as defined above). The caster acts as a third wheel for your robot and should allow it to easily move in any direction.

The caster should be designed in such a way that the bearing does not easily slip out of the caster. It should also be designed in such a way that the bearing can roll easily inside the caster. Finally it needs to be designed so that the caster does not break when inserting or removing the bearing. The following are useful guidelines.

Covers at least 200 degrees but no more than 300 degrees total of the sphere. 
Has a shell thickness of at least .06”
Has an inner diameter .03” larger than the diameter of your ball bearing
Has at least three expansion cuts of at least 60 degree arc
Includes a brass insert for mounting to robot frame. (see brass insert in engineering concepts)
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
