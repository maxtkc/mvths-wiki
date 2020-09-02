# Midi

## Overview

MIDI is a communication and file format that can be used to control specific instruments and devices

# ttyMIDI

ttyMIDI is a command line tool that creates a ports for connecting MIDI to external devices and internal players.

## Install

1.  Download the latest version of the source code from github.
2.  Unzip the file into your home directory
3.  Install libsound2-dev using the following command.

#### $ apt-get install libasound2-dev

4.  Modify the Make file by adding -lpthread to the end of the gcc line

#### gcc src/ttymidi.c -o ttymidi -lasound -lpthread

5.  Run make from inside the directory created by ttyMIDI

#### $ sudo make install

## Port Connection

You can connect to a port using the following command. Note that you will need to put in a specific port name for NAMEOFPORT.

#### $ ttymidi -s /dev/ttyNAMEOFPORT

For example if you want to send data to a Arduino device, plug in that device and ls the ports using the following command.

#### $ ls /dev/tty\*

This will list all ports with the tty prefix. You should see either ttyACM0 or ttyUSB0. Unplug your Arduino device and run the ls command again. Either ttyACM0 or ttyUSB0 should disappear. This will tell you which device you have plugged into your port.

Once you know what port you are using, you can connect ttyMIDI to that port. The following is an example.

#### $ ttymidi -s /dev/ttyUSB0 -b 57600 &

This will connect ttyMIDI to port ttyUSB0 at a baud rate of 57600. The & runs the program in the background so you do not have to launch another window. The baudrate flag is optional. If you do not include this flag ttyMIDI defaults to a baudrate of 115200.

Note that it might be more convenient to run the command without the & and in its own window. This way it does not hold the serial port open when you try to program your device and you can close it easily with ctrl-c.:

To test if ttymidi is connected to and output port you can run the following command.

#### $ aconnect -o

Try running this command before and after running ttymidi to see the difference in return values. If the tty port gets stuck and only returns USB1 than you can kill the job as shown above.
