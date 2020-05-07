# Overview

In this lesson, you will learn to set up a Raspberry Pi (RPI) single board computer.

# Format OS

In order to use your Raspberry Pi you will need to install an operating system (OS) on the RPI. The OS you will be using is Raspian Lite which is a derivative of the Linux OS.

 

1.  Download the latest version of [Raspian Lite](https://www.google.com/url?q=https://www.raspberrypi.org/downloads/raspbian/&sa=D&ust=1587613174396000) and save it in your downloads directory.
2.  Once you have downloaded Raspian Lite, extract the file into its own directory.
3.  Insert a microSD card into your computer. If your computer does not have a microSD card reader, you will need to use a USB card reader.  
4.  Format the OS onto the microSD card. Launch [balenaEtcher](https://www.google.com/url?q=https://www.balena.io/etcher/&sa=D&ust=1587613174397000) and select Raspian Lite as the selected image. Select the microSD card as the selected drive.
5.  Note: You will need administrative privileges to create an image.

# Setup SSH

In order to access your RPI you will need to use SSH. The SSH protocol (also referred to as Secure Shell) is a method for secure remote login from one computer to another. It provides several alternative options for strong authentication, and it protects the communications security and integrity with strong encryption. It is a secure alternative to the non-protected login protocols (such as telnet, rlogin) and insecure file transfer methods (such as FTP).You can learn more about SSH [here](https://www.google.com/url?q=https://www.ssh.com/ssh&sa=D&ust=1587613174397000).

Once your microSD is completely formatted you will need to add one file to the top level of the boot directory. The file should be named “ssh” and should have no extension. Make sure you have extensions visible in your windows manager. This file tells the OS to enable SSH.

# Setup RPI

1.  Plug the microSD card into the RPI. Note that the microSD card acts as the hard drive on your computer.
2.  Power up the RPI using an approved power supply.
3.  Connect the RPI to an ethernet port using an ethernet cable.

# SSH to RPI

The next step is to SSH into the RPI. Through SSH you will be logged into the RPI and have complete user privileges. In order to do this you will first need to determine the IP address of your RPI. All of the computers and many other devices such as your phone or printers have a unique IP address provided by the school’s routers. These addresses take the form of four 8-bit numbers separated by periods. A typical address in our school would look like 10.1.41.22

Unique addresses provide a way to independently address every device in the school. Note that most devices do not allow for SSH access in order to protect themselves from getting hacked. The  school routers generally assign the same device the same address, i.e. if you unplug your device from the network and plug it in again tomorrow, it is likely (but not necessarily) to receive the same IP address. You can learn more about IP addresses [here](https://www.google.com/url?q=https://www.paessler.com/it-explained/ip-address&sa=D&ust=1587613174398000).

The router does this by knowing the MAC address of your device. While IP addresses are assigned by a router, a MAC address is assigned by a manufacturer and every single connected device in the world as a unique MAC address. MAC addresses are made up of six 8-bit numbers giving a combination of 281,474,976,710,656 discrete values. If we create more devices than that we are in trouble. You can learn more about MAC addresses [here](https://www.google.com/url?q=https://www.geeksforgeeks.org/introduction-of-mac-address-in-computer-network/&sa=D&ust=1587613174399000).

# Find IP Address

In order to find your RPI on the network, you will need to find what IP address it has been assigned by your router. One way to do this is using Advanced IP Scanner which is installed on your machine. Since our router assigns addresses in the range of  10.1.41.1 - 10.1.41.150, I recommend writing this range into the scan window in the main interface.

When the scan is complete scroll down until you find devices listed under the manufacturer RPI Foundation. If there is more than one device, you might need to unplug your device and run the scan again to see if it shows up thereby determining which device is yours.

If you have access to a computer running Linux you can run the following command from the command line

#### sudo nmap 10.1.41.1-100 -sn |grep -B 2 -i raspberry

# Login Using SSH

Windows: From a windows machine launch the console editor cmder. You can find this installed on your computer. At the command prompt type the following using the address you found. The RPI will respond asking for a password. The default password for the RPI is raspberry.

#### $ ssh pi@10.1.41.2

# Update OS

Once you are logged into the RPI for the first time you should make sure to update the software. Unlike Windows, all important Linux system software and user software is stored on repositories around the world and very easily accessible. The first command listed below will make sure that your OS is looking at the most updated repositories for software available. The second command will update all of your software to the latest stable version. It is useful to periodically run these commands to make sure your software is up to date.

####         $ sudo apt-get update

####         $ sudo apt-get upgrade
