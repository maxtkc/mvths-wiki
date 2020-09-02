Rpi Router
==========

1. Download image

.. raw:: html

   <!-- end list -->

1. Go to the openWRT
   `website <https://www.google.com/url?q=https://openwrt.org/&sa=D&ust=1587613174497000>`__.
2. Look under the downloads and select Stable Releases
3. Look under brcm2708 and then bcm2710
4. Download the factory file (this name might change)

.. raw:: html

   <!-- end list -->

2. Initial login

.. raw:: html

   <!-- end list -->

1. Connect router direct via ethernet to Linux machine
2. ssh root@192.168.1.1 (no password)

.. raw:: html

   <!-- end list -->

3. Set password

Use the following command to create a password. Create a password of
over eight characters.

root@OpenWrt:~# passwd
----------------------

4. Setup network

The DHCP should be set to request a dynamic address upstream. Later this
can be changed to a static address, but address must first be confirmed
with network admin.

3. View existing network configuration with:

root@OpenWrt:~# cat /etc/config/network
---------------------------------------

                or

root@OpenWrt:~# uci show network
--------------------------------

4. Make the following changes. This will set the router to grab a
   dynamic IP address instead of setting a static IP address

uci delete network.lan.ipaddr
-----------------------------

| uci delete network.lan.netmask
| uci delete network.lan.ip6assign
| uci set network.lan.proto=dhcp

5. Commit the changes

uci commit network
------------------

6. NOTE: The following might be useful. Need to research these options.

uci set network.lan.ipv6=0
--------------------------

| uci set network.lan.ifname='eth0 eth1'
| uci set network.lan.stp=1

uci delete network.globals.ula\_prefix
--------------------------------------

uci delete network.@switch\_vlan[1]

5. Setup router on network.

.. raw:: html

   <!-- end list -->

1. Connect router to network
2. Scan for router’s IP
3. ssh into router

.. raw:: html

   <!-- end list -->

6. Update packages

Installing LuCI is not necessary but provides a GUI for the router.

opkg update
-----------

opkg install vim
----------------

opkg install luci
-----------------

7. Setup DHCP

You need to disable the assignment of addresses (downstream) via DHCP in
order to ensure that there are no conflicts between the new router and
the existing routers.

1. View existing configuration

root@OpenWrt:~# cat /etc/config/dhcp
------------------------------------

                Or

root@OpenWrt:~# uci show dhcp
-----------------------------

2. Disable downstream DHCP

uci set dhcp.lan.ignore=1
-------------------------

3. Commit changes.

uci commit dhcp
---------------

8. Setup wireless

.. raw:: html

   <!-- end list -->

1. View existing configuration

root@OpenWrt:~# cat /etc/config/wireless
----------------------------------------

                Or

root@OpenWrt:~# uci show wireless
---------------------------------

2. Enable wireless

        Turn on the wireless and set encryption values.

uci set wireless.radio0.disabled=0
----------------------------------

uci set wireless.default\_radio0.encryption=psk2
------------------------------------------------

uci set wireless.default\_radio0.key=mvthsstudent
-------------------------------------------------

uci commit wireless
-------------------

wifi down
---------

wifi up
-------

RPI Bluetooth

sudo apt-get install bluetooth blueman bluez
--------------------------------------------

This installs all the software necessary for using bluetooth on RPP

sudo reboot
-----------

This gets the service running

sudo apt-get install python-bluetooth
-------------------------------------

This installs the python bluetooth

sudo apt-get install python-rpi.gpio
------------------------------------

This is for the gpio but is likely already installed

sudo bluetoothctl
-----------------

This gets the bluetooth running

[bluetooth]# power on
---------------------

[bluetooth]# agent on
---------------------

[bluetooth]# discoverable on
----------------------------

[bluetooth]# pairable on
------------------------

[bluetooth]# scan on
--------------------

In order to see the device it must be running bluetooth...not sure why,
but need to open the BT on the Android and then hit more settings for
the scan to find the Android. It finds it under Nexus.

pair <address of your phone>
----------------------------

This will pair the devices

[bluetooth]# info <address of your phone>
-----------------------------------------

This will provide the status of your device. It should show that it is
paired but not connected. Connection only happens when you run a script
to connect such as the python script.

[bluetooth]# remove <address of your phone>
-------------------------------------------

This can remove your device. You must rescan and find the device before
you can pair it again.

Here is python script for pairing.

import bluetooth
----------------

import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI
----------------------------------------------------------------------------------------

LED=21
------

 
-

GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
-------------------------------------------------------------------------------------------

GPIO.setwarnings(False)
-----------------------

GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
-------------------------------------------------------------------

GPIO.output(LED,0)
------------------

 
-

server\_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
------------------------------------------------------------

 
-

port = 1
--------

server\_socket.bind(("",port))
------------------------------

server\_socket.listen(1)
------------------------

 
-

client\_socket,address = server\_socket.accept()
------------------------------------------------

print "Accepted connection from ",address
-----------------------------------------

while 1:
--------

 
-

 data = client\_socket.recv(1024)
---------------------------------

 print "Received: %s" % data
----------------------------

 if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
----------------------------------------------------------------------------

  print ("GPIO 21 LOW, LED OFF")
--------------------------------

  GPIO.output(LED,0)
--------------------

 if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
----------------------------------------------------------------------------

  print ("GPIO 21 HIGH, LED ON")
--------------------------------

  GPIO.output(LED,1)
--------------------

 if (data == "q"):
------------------

  print ("Quit")
----------------

  break
-------

 
-

client\_socket.close()
----------------------

server\_socket.close()
----------------------

WHO IS ON
---------

iwinfo wlan0 assoclist

U4VL WEBRTC

Overview
--------

U4VL is a method for video capture and streaming that works with WebRTC.

Set Up
------

Use the following curl command to get access to the packages.

$ curl http://www.linux-projects.org/listing/uv4l\_repo/lpkey.asc \| sudo apt-key add -
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following line to /etc/apt/sources.list to also add access to
the repositories.

deb http://www.linux-projects.org/listing/uv4l\_repo/raspbian/stretch stretch main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next run an update and upgrade to make sure you have all the latest
resources

$ sudo apt update
~~~~~~~~~~~~~~~~~

$ sudo apt upgrade
~~~~~~~~~~~~~~~~~~

Install
-------

The following installs the base packages and can be used to for taking
snapshots and maybe other purposes. Not sure. Should be tested.

$ sudo apt install uv4l uv4l-raspicam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following provides easy access to turning on and off the camera.

$ sudo apt install uv4l-raspicam-extras
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once this is installed you can use:

$ sudo service uv4l\_raspicam status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

$ sudo service uv4l\_raspicam restart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

$ sudo service uv4l\_raspicam stop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This installs a way to access streaming service remotely.

$ sudo apt uv4l-server
~~~~~~~~~~~~~~~~~~~~~~

This last installs a WebRTC. This provides GUI access but I think also
makes it work with other video services.

$ sudo apt uv4l-webrtc
~~~~~~~~~~~~~~~~~~~~~~

Configuration
-------------

In order to configure the settings you can edit the
/etc/uv4l/uv4l-raspicam.conf file. The following changes to the settings
seemed to work. Also, you can establish settings at the command line.

encoding = h264

width = 1640

height = 1232

framerate = 4

custom-sensor-config = 4

Bitrate = 2000000

NOTE: Still not sure how to avoid having it auto start on reboot!
