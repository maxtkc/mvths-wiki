# Install Particle Cli

Linux

Install Latest version of node

curl -sL https://deb.nodesource.com/setup\_10.x | sudo -E bash -  
sudo apt-get install -y nodejs

This first command must be done as root\!

how to install the particle-cli  
$ npm install -g particle-cli  
$ particle login

Use your password

particle setup

NOT WORKING\!\!\!\!\!\!\!

Windows

Npm install -g --unsafe-perm particle-cli

MAC Address

In order to find the MAC address the firmware must be up to date. Update firmware with the command photon in DFU mode and entering

#### particle update

It appears the only way to check MAC address is with the serial monitor in Particle Desktop

Put the photon in listening mode

m for mac address

i for device ID

v for version

NEW USER

#### useradd -m -s /bin/bash username

M flag sets up home directory

S flag makes sure it is using bash

SSD1306

For Photon using the default code in the Libraries. The following connections work

MOSI = A5

CLK = A3

RST = D5

CS = D4

DC = D3

#### passwd username

#### whoami

#### usermod -s /bin/bash username

#### echo $SHELL

# Recording Sound

The following is example code that can be used to record the duration of button presses and play them back. The example code is can only record five durations, but the code can be set to record any number.

unsigned long duration\[7\];

int count, next, last;

void setup() {

  pinMode(7, INPUT\_PULLUP);

}

void loop() {

  int y = digitalRead(7);  //READ BUTTON

  if (y == LOW ) {  //IF BUTTON IS PRESSED

    next = millis();  //STORES LAST READING FROM TIMER

    duration\[count++\] = next - last;  //STORES DIFF BETWEEN PRESENT

                                                         AND LAST READING

    last = next;  //SETS THE PRESENT READING AS THE LAST READING

    tone(3, 440, 100);  //PLAYS A TONE

    delay(200); //ADDS A DELAY FOR THE BUTTON PRESS

  }

  if (count == 5) {  //IF THE USER HAS PRESSED THE BUTTON FIVE TIMES

    delay(1000);  //CREATE A PAUSE BEFORE PLAYING THE STORED SOUND

    for (int x = 1; x \<= 5; x++) {  //PLAY THE FIVE TONES

      tone(3, 440, 100);  //PLAY TONE

      delay(duration\[x\]); //WAIT THE RECORDED DURATION

    }

    count = 0; //RESET THE COUNT TO ZERO FOR THE NEXT RECORDING

  }

}
