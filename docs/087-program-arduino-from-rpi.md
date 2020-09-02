# Program Arduino From Rpi

## Overview

In this lesson, you will learn how to program your Arduino directly from the RPI. This will make working with both devices together much easier\!

## Installing Arduino-CLI

The easiest way to get and install the latest version of the Arduino CLI on any supported platform is using  curl with an install script.

1.  Check if curl is installed by typing curl at the command line. If not, install curl with the following command.

#### $ sudo apt install curl

2.  Navigate to your home directory.
3.  Create a new directory called Arduino.
4.  Navigate into the new Arduino directory
5.  Run the following command at the command line. This will create a bin directory in side your home directory. The arduino-cli can be found inside this directory.

#### $ curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh

## Path to Arduino

In order for you to be able to run arduino-cli from any directory, you will need to record a path to arduino-cli in your .bashrc.

1.  As a test, type the following at the command line. It should produce an error command not found. This is because your system does not know where to find arduino-cli.

#### $ arduino-cli

2.  Open .bashrc. Note that the \~ is a shortcut to your home directory i.e. /home/yourname

#### $ vi \~/.bashrc

3.  Add the following line to the end of the file. This will tell the system where to look when you use the command arduino-cli. Important: The path is simply the complete path to the new bin directory that you just installed. The path shown below would be typical for an RPI. If you are using your personal linux computer you might have a different path. For example, pi might be replaced with your name.

#### export PATH=”/home/pi/Arduino/bin:$PATH”

4.  Quit out of the .bashrc file
5.  Apply the changes you made to your .bashrc using the following command.

#### $ source \~/.bashrc

6.  As a test, again type the following command in your terminal. The response should now provide detailed information about the program.

#### $ arduino-cli

## Configuration Script

The next step is to install a configuration script for the arduino-cli. Depending on which board you are using you may or may not need to use this file, but it is best to install it anyway.

1.  Navigate to your home directory.
2.  Run the following command. This will create a .arduino15 directory in your home directory. The configuration can  be found inside this directory.

#### $ arduino-cli config init

## Installing your Board File

The next step is to install the correct board file for your arduino-cli. If you are using an Arduino Uno or another standard Arduino branded board the process is fairly simple. If you are using an off-brand Arduino device such as the Metro Mini, the process takes a few more steps.

## Board File (Arduino-branded devices)

Step one is to update the core index of devices by running the following command. The command and the expected result are shown below.

#### $ arduino-cli core update-index

#### Updating index: package\_index.json downloaded

The next step is to plug in your board to the USB port of your computer and run the following command. Note that you may see many ports listed in addition to the one connected to your board. Using more will allow you scroll through the list more easily.

#### 

#### $ arduino-cli board list

#### Port   Type        Board Name              FQBN                 Core

#### /dev/ttyACM1 Serial Port (USB) Arduino Uno arduino:avr:uno arduino:avr

If this all worked for you, you can move on to the steps for compiling and programming. If not, follow the steps for non-branded devices.

## Board File (off-branded devices)

The following steps are specifically for the Meto Mini but should work with other off-brand boards as well.  

1.  Run the following command to list all installed boards and you will notice that the Metro is not listed.

#### $ arduino-cli board listall

2.  Execute the following command which dumps the results of the configuration file.  The line that includes “additional\_urls” should be blank. In order for the arduino-cli to find board files for the Metro you will need to modify this line.

#### $ arduino-cli config dump

3.  Open the arduino-cli.yaml configuration file which can be found in your home directory under the .arduino15 directory.
4.  Modify the “additional\_urls” line so that it looks like the following. This will allow the arduino-cli to look for cores from the Adafruit packages.

####  additional\_urls: https://adafruit.github.io/arduino-board-index/package\_adafruit\_index.json

5.  Save and close the file and run the configuration command (See above) again. This time you should see the correct additional url listed.
6.  Run the command for updating the core again. You should see that the Adafruit cores are now included in the update.

#### $ arduino-cli core update-index

7.  Run the following command again and you should now see the metro listed.

#### $ arduino-cli board listall

8.  You will now need to install the core for the adafruit:avr

#### $ arduino-cli core install adafruit:avr

9.  You will also need to install the core for the arduino:avr

#### $ arduino-cli core install arduino:avr

10. Once this is complete, running the listall command again should show your device

#### $ arduino-cli board listall

11. Note that running the following command should now list your device if it is connected through USB but in my experience this does not work. The board can still be used though.

#### $ arduino-cli board list

## Creating a New Sketch

Now you are ready to create your first sketch. This can be accomplished with the simple command shown below. You may place your sketches wherever you like, but I recommend creating a directory Documents for all of your Arduino sketches.

#### $ arduino-cli sketch new MyFirstSketch

## Compiling and Programming

To compile your program, first make sure you are in the same directory as the code file you just created. Then run the following. Note that the arguments for the --fqbn flag will depend on your device.

$ arduino-cli compile --fqbn arduino:arv:metro

To program your device run the following command. Again, adjust the arguments for --fqbn flag for your specific device.

$ arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:metro

## Port Permissions

If you run into permission problems with accessing your port you will need to do the following. The first step is to determine which groups the port you are using belongs to. Note that the ls command is for listing details. The l flag is for long format and the a flag makes sure to list hidden files.

#### $ ls -la /dev/ttyUSB0

#### crw-rw---- 1 root dialout 188, 0 Apr  1 12:36 /dev/ttyUSB0

For the returned values shown above, the owner is root, the group is dialout and both the owner/group have read/write permissions. Now list the groups for your user by typing groups at the command line.

#### $ groups

#### sam adm cdrom sudo dip plugdev lpadmin sambashare

For the returned values above you can see that the user sam belongs to eight groups, but not the dialout group. You can add your user to the dialout group with the following command. Replace $USER with your username.

#### $ sudo usermod -a -G dialout $USER

Once you have completed this, you will need to log out and log back in for the changes to take effect. To confirm the changes type groups at the command line. This time you should see dialout as one of your groups.

### Challenge

Write a program to count up by one every second on a four digit LED display.

TEACHER CHECK \_\_\_\_

## Adding Libraries

Many of the advanced programs you write or the advanced components will need custom libraries that are not pre-installed. In order to install a custom library, you will need to first find the name of the library. For example to search for all libraries including the word LED, you would enter the following command in any directory.

#### $ arduino-cli lib search LED

Note that this will produce the name of all the libraries as well as many details about each library. If you just want to see the names use grep as shown below.

#### $ arduino-cli lib search LED | grep Name:

Once you have the name of the library you can install that library from any directory. All of the libraries should be stored in an automatically created directory titled “library” and found in the directory where you store all of your projects. If this is not the case, you should make sure the directory paths in your arduino-cli.yaml are set correctly.

#### $ arduino-cli lib install “Adafruit\_LED\_backpack”
