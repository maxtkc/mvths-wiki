Setting Up Serial On Rpi
========================

Overview
--------

In this lesson, you will set up the serial communication drivers on your
RPI. Using serial communication, your RPI can directly communicate with
as well as program an Arduino over the USB port.

Enable Serial
-------------

In order to use serial communication with your RPI, you must enable the
serial communication on your RPI.

1. From the command shell, run sudo raspi-config 
2. Choose Interfacing Options from the menu and then choose Serial.
3. At the first dialog box, “Would you like a login shell to be
   accessible over serial?” select No.
4. At the second dialog box, “Would you like the serial port hardware
   enabled?” select Yes.
5. Select OK and Finish.

Get Port Address
----------------

In order to use your serial port you will need to know the address
assigned to it by the RPI.

1. Unplug your Arduino from the RPI
2. Run ls /dev/tty\* This should provide a list of ports.
3. Plug your Arduino into the RPI and run the above command again. Make
   note of which port is only visible when the Arduino is plugged in.
   Note that the address will look like ttyACM0.
4. The same process will work with a Metro Mini. The only difference is
   that the address will look like ttyUSB0

SERIAL (ARDUINO TO RPI)

Overview
--------

In this lesson you will learn how to send and receive data using the
serial port.

Arduino Code
------------

The first step is to program your Arduino to send a repeated value to
the RPI using 9600 baud rate.

1. Create a new directory for your Arduino project.
2. In this directory create a new code file as shown below. Upload this
   file to your Arduino.

void setup() {
~~~~~~~~~~~~~~

    Serial.begin(9600);
~~~~~~~~~~~~~~~~~~~~~~~

}
~

void loop() {
~~~~~~~~~~~~~

  Serial.println(“367”);
~~~~~~~~~~~~~~~~~~~~~~~~

  delay(500);
~~~~~~~~~~~~~

}
~

(Virtual Environment)
---------------------

If you have not already done so, set up a virtual environment for this
new Python project. If you are not familiar with virtual environments
check out the previous lesson on setting up virtual environments.

Installing pySerial
-------------------

If you have not already done so, install pyserial into your virtual
environment using pip.

(env) $ pip install pyserial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python
------

Create the following code file and store it in your virtual environment.

import serial
~~~~~~~~~~~~~

ser = serial.Serial('/dev/ttyACM0', 9600)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while 1:
~~~~~~~~

    line = ser.readline()
~~~~~~~~~~~~~~~~~~~~~~~~~

    print(line)
~~~~~~~~~~~~~~~

At the command line run the file and you should see the data from the
Arduino displayed in your screen.

SERIAL (RPI TO SERIAL)

Arduino
-------

In order to view what you are sending to the Arduino, it will be helpful
to have a display. In the following example you will be using a
7-segment matrix display. You can find more information about how to use
under matrix display in this guide.

1. Connect the four-digit 7-segment display to the Arduino.
2. Install the Adafruit\_LEDBackpack and Adafruit\_GFX libraries onto
   your RPI, if you have not already done this. Read
   `here <https://www.google.com/url?q=https://arduino.github.io/arduino-cli/getting-started/&sa=D&ust=1587613174441000>`__ for
   information about how to do this.
3. Upload the following code to your Arduino from your RPI

#include <Wire.h>                                                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#include <Adafruit\_GFX.h>                                          
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#include "Adafruit\_LEDBackpack.h"                                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adafruit\_7segment matrix = Adafruit\_7segment();                    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

String inString = "";                                              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void setup() {                                                      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        matrix.begin(0x70);                                        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        matrix.print(0, DEC);                                      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        matrix.writeDisplay();                                      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Serial.begin(9600);                                        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

}                                                                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                                                                                           
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void loop() {                                                      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if (Serial.available()) {                                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                int inChar = Serial.read();                        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                if (isDigit(inChar)) {                              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                        inString += (char)inChar;                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                }                                                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                if (inChar == '\\n') {                              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                        matrix.print(inString.toInt(), DEC);        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                        matrix.writeDisplay();                      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                        inString = "";              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               
~~~~~~~~~~~~~~~

                }                                                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        }                                                          
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

}                                                                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RPI
---

The following is the python code that will send a number to your Arduino
that increments by one every half second. For more information about how
to format serial strings read
`here <https://www.google.com/url?q=https://pyformat.info/&sa=D&ust=1587613174445000>`__.

import serial
~~~~~~~~~~~~~

import time
~~~~~~~~~~~

count = 0
~~~~~~~~~

ser = serial.Serial('/dev/ttyACM0', 9600)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while 1:
~~~~~~~~

    count+=1
~~~~~~~~~~~~

    ser.write('{:d}\\n'.format(count))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    time.sleep(.5)
~~~~~~~~~~~~~~~~~~

TSP

1. Download image
2. Open in GIMP
3. Remove all background space
4. Scale the image to correct width of pixels

.. raw:: html

   <!-- end list -->

1. Image/Scale Image

.. raw:: html

   <!-- end list -->

5. Convert image to greyscale

.. raw:: html

   <!-- end list -->

1. image/mode/greysacle

.. raw:: html

   <!-- end list -->

6. Washout the image

.. raw:: html

   <!-- end list -->

1. Colors/levels
2. Set all channels to 200

.. raw:: html

   <!-- end list -->

7. Stipple image

.. raw:: html

   <!-- end list -->

1. Image/mode/indexed
2. Use black and white 1bit palet
3. Remove unused colors from colormap
4. Color dithering Floyd-Steinberg Normal

.. raw:: html

   <!-- end list -->

8. Save as PBM

.. raw:: html

   <!-- end list -->

1. Maker sure add .pbm extension and save as ascii
2. `Link <https://www.google.com/url?q=https://wiki.evilmadscientist.com/Producing_a_stippled_image_with_Gimp&sa=D&ust=1587613174448000>`__
   for more info.

.. raw:: html

   <!-- end list -->

9. Open file in Vim

.. raw:: html

   <!-- end list -->

1. :%s/.\\{50}/&\\r/g (place hard return at 50)
2. :%s/\\n//g (remove all line breaks)

Javascript
----------

Javascript is a powerful language for controlling devices.

1. Set up a json package using the following command. This will be
   useful for installing nodejs serial. Make sure you have already
   installed Nodejs.

npm init --yes

2. Run the following serial installer

sudo npm install serialport --unsafe-perm --build-from-source

Particle CLI
------------

As root:

apt install dfu-util
~~~~~~~~~~~~~~~~~~~~

apt install nodejs
~~~~~~~~~~~~~~~~~~

apt install npm
~~~~~~~~~~~~~~~

npm install -g particle-cli
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update
------

When you first log into your RPI, you should run the following commands
to make sure it is up to date.

INSTALL VIM
-----------

LEARN VIM

RESET ESC/CAPS

Modify

 /etc/default/keyboard
~~~~~~~~~~~~~~~~~~~~~~

XKBOPTIONS="caps:swapescape"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Particle compile photon blink.ino
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Particle flash name-of-photon name-of-file.bin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install Cert
------------

In order to access sites outside the school using any communication
protocol, you will need to install a certificate.

1. Copy the certificate from your local directory to the RPI using scp.
   If you do not know how to use scp, you can find a reference in this
   guide.
2. Place the cert under  /usr/share/ca-certificates
3. Add your cert name to the bottom of the ca-certificates.conf file
   which can be found in the /etc directory.  
4. Update certificates using the following command.

sudo update-ca-certificates –-fresh

Install Nodejs (optional)
-------------------------

Nodejs is useful for running many javascript packages.

1. Download the Nodejs source package

curl -sL "https://deb.nodesource.com/setup\_8.x" \| sudo -E bash -

2. Install Nodejs and necessary packages (the g flags ensures that
   everything is installed globally)

sudo apt install nodejs

| sudo apt-get update && sudo apt-get upgrade
|         sudo apt-get install build-essential
|         sudo npm install -g npm

| NOTE: You must become root using  sudo su before running the following
  command.
|         sudo npm install -g onoff

NOTE: To return to from root type exit

JSON Parse in Python

import urllib, json

url = "https://api-v3.mbta.com/routes"

response = urllib.urlopen(url)

data = json.loads(response.read())

#formated\_data = data['data'][3]['id']

formated\_data = data['data'][0]['attributes']['color']

print(formated\_data)

RPI to Arduino (Arduino side)
-----------------------------

In order to view what you are sending to the Arduino, it will be helpful
to have a display. In the following example you will be using a
7-segment matrix display. You can find more information about how to use
under matrix display in this guide.

4. Connect the 7-segment matrix display to the Arduino.
5. Make a new directory in your sketchbook or modify an existing sketch.
6. Copy the following code into your file.

#include <Wire.h>                                                  

#include <Adafruit\_GFX.h>                                          

#include "Adafruit\_LEDBackpack.h"                                  

                                                                   

Adafruit\_7segment matrix = Adafruit\_7segment();                    

                                                                   

String inString = "";                                              

                                                                   

void setup() {                                                      

        matrix.begin(0x70);                                        

        matrix.print(0, DEC);                                      

        matrix.writeDisplay();                                      

        Serial.begin(9600);                                        

}                                                                  

                                                                       
                                                   

void loop() {                                                      

                                                                   

        if (Serial.available()) {                                  

                int inChar = Serial.read();                        

                if (isDigit(inChar)) {                              

                        inString += (char)inChar;                  

                }                                                  

                if (inChar == '\\n') {                              

                        matrix.print(inString.toInt(), DEC);        

                        matrix.writeDisplay();                      

                        inString = "";              

               

                }                                                  

        }                                                          

}                                                                  

7. Download code to Arduino.

RPI to Arduino (RPI side)
-------------------------

The following is the python code that will send a number to your Arduino
that increments by one every half second. For more information about how
to format serial strings read
`here <https://www.google.com/url?q=https://pyformat.info/&sa=D&ust=1587613174460000>`__.

import serial

import time

count = 0

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:

    count+=1

    ser.write('{:d}\\n'.format(count))

    time.sleep(.5)
