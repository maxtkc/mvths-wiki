# Overview

Websockets provide an excellent way to perform real time communication between a server and client. The following example demonstrates using a websocket to communicate between a PC client connected to a joystick and a RPI connected to an Arduino and display. The PC yoystick client sends the data from the joystick. The PC web client gets data from the Arduino.

# Server

The following is an example of the server code that would run on the RPI.

\#\!/usr/bin/env python  
\# WS server example  
  
import asyncio  
import json  
import serial  
import time  
import websockets  
  
\#create serial object  
ser = serial.Serial('/dev/ttyACM0', 9600)  
  
\#clear input serial buffers  
ser.reset\_input\_buffer()  
  
\#create a set to store websocket connections  
connected = set()  
  
\#Receiver runs continuously  
async def hello(websocket, path):  
   \#add each connection to the list  
   connected.add(websocket)  
   \#use to enable continuous connection to socket  
   async for message in websocket:  
       y = json.loads(message)  
       x = y\["Axes"\]\[0\]  
       x = int(x \* 1000)  
       print(x)  
       ser.write('B{}\\n'.format(x).encode())  
  
\#Sender is called once and runs in the background  
async def world():  
   while True:  
       \#check if data is available in the websocket  
       if (ser.in\_waiting \> 0):  
           data = ser.read(ser.in\_waiting).decode('ascii')  
           print (data)  
       \#removes unused sockets after they disconnect  
       for websocket in connected.copy():  
           try:  
               await websocket.send(data)  
           except:  
               connected.remove(websocket)  
       await asyncio.sleep(1)  
  
start\_server = websockets.serve(hello, "0.0.0.0", 8765, ping\_interval=None)  
asyncio.get\_event\_loop().run\_until\_complete(start\_server)  
asyncio.ensure\_future(world())  
asyncio.get\_event\_loop().run\_forever()  

# Client (joystick)

The following is an example of client code that would reside on a PC. This client sends data in real time from a joystick to the server.

\#\!/usr/bin/env python  
  
import asyncio  
import pygame  
import websockets  
import json  
import time  
  
\#initialize pygame  
pygame.init()  
\#initialize joystick  
pygame.joystick.init()  
  
\#create and initialize one joystick object  
stick = pygame.joystick.Joystick(0)  
stick.init()  
  
uri = "ws://192.168.1.9:8765"  
\#interval must be set to none or the client dies without a regular response from server  
websocket = websockets.connect(uri, ping\_interval=None)  
  
async def joy():  
  
   global websocket  
   async with websocket as websocket:  
       while True:  
       \#request update of joystick status  
               pygame.event.pump()  
               axes = stick.get\_numaxes()  
               axis\_values = \[0\] \* axes  
               for i in range(axes):  
                   axis\_values\[i\] = stick.get\_axis(i)  
               \#send all four axis value packaged as json  
               await websocket.send(json.dumps({"Axes": axis\_values}))  
               \#delay necessary to prevent overload of receiver, adjust as necessary  
               time.sleep(.1)  
  
asyncio.get\_event\_loop().run\_until\_complete(joy())  
pygame.joystick.quit()  

# Client (browser)

The following is client code that allows you to use a browser to see data sent from the server.

\<\!DOCTYPE html\>  
\<html\>  
   \<head\>  
       \<title\>WebSocket demo\</title\>  
   \</head\>  
   \<body\>  
       \<script\>  
           var ws = new WebSocket("ws://192.168.1.9:8765/"),  
                messages = document.createElement('ul');  
            ws.onmessage = function (event) {  
               var messages = document.getElementsByTagName('ul')\[0\],  
                    message = document.createElement('li'),  
                    content = document.createTextNode(event.data);  
                message.appendChild(content);  
                messages.appendChild(message);  
           };  
           document.body.appendChild(messages);  
       \</script\>  
   \</body\>  
\</html\>  

# Arduino

The following is coordinated code that runs on the Arduino.

\#include \<Adafruit\_NeoPixel.h\>  
\#include \<Adafruit\_LEDBackpack.h\>  
\#include \<avr/power.h\>  
  
\#define PIN         13  
\#define NUMPIXELS   8     
\#define WAIT        0  
\#define READ\_VALUE  1  
\#define BUTTONA     2  
\#define PRESSED     LOW  
  
Adafruit\_7segment matrix = Adafruit\_7segment();  
Adafruit\_NeoPixel pixels = Adafruit\_NeoPixel(NUMPIXELS, PIN, NEO\_GRB + NEO\_KHZ800);  
  
uint32\_t thisTime = 0, lastTime = 0;  
int state = WAIT;  
String inString = "";  
char inCmd;  
  
void set\_pixels(uint8\_t value) {  
   for (int x=0; x\<8; x++) {  
  
       if (value & (1\<\<x)) {  
           pixels.setPixelColor(x, pixels.Color(50,0,0));  
       }  
       else {  
           pixels.setPixelColor(x, pixels.Color(0,0,0));  
       }  
   }  
   pixels.show();  
}  
  
void run\_cmd(char cmd, int value) {  
   if (cmd == 'A')  
       set\_pixels(value);  
   else if (cmd == 'B') {  
       matrix.print(value, DEC);  
       matrix.writeDisplay();  
   }  
  
  
}  
  
  
void setup(){  
   Serial.begin(9600);  
  
   matrix.begin(0x70);  
   matrix.print(0, DEC);  
   matrixd.writeDisplay();  
  
   pixels.begin();  
   set\_pixels(0x00);  
  
   pinMode(BUTTONA, INPUT\_PULLUP);  
}  
  
  
void loop() {  
   if (Serial.available()) {  
       int inChar = Serial.read();  
       if (state == READ\_VALUE) {  
           if (isDigit(inChar))  
               inString += (char)inChar;  
           else if (inChar == '\\n') {  
               int inValue = inString.toInt();  
               run\_cmd(inCmd, inValue);  
               inString = "";  
               state = WAIT;  
           }  
       }  
       else if (state == WAIT) {  
           if (isUpperCase(inChar)) {  
               inCmd = (char)inChar;  
               state = READ\_VALUE;  
           }  
       }  
   }  
   thisTime = millis();  
   if (thisTime - lastTime \>= 1000) {  
       int aVal = analogRead(3);  
       if (BUTTONA == PRESSED)  
               bVal = true;  
       else  
               bval = false;  
       Serial.print(y);  
       lastTime = thisTime;  
   }  
}  
  
