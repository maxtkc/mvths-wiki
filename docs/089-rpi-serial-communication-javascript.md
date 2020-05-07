# Test Serial for Node

Create a javascript file with the following code. In your Arduino write a program that sends a data value and the data value that it receives. After running the file, you should see the serial data from your Arduino show up in the console.

        //Include the Serialport library

var SerialPort = require("serialport");

//Create an instance of the serial port monitor        

var serialport = new SerialPort("/dev/ttyACM0", 9600);  

//Define function for the open event

serialport.on('open', onOpen);

//Define function for the receive data event

serialport.on(‘data’, onData);

//Listener that responds to on open event              

function onOpen() {  

console.log('Serial Port Is Open');                                              

}  

//Listener that responds to receive data event    

function onData(d) {

console.log(“Data: “ + d);

serialport.write(‘r’);

}                                      
