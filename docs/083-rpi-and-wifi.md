# Rpi And Wifi

## Steps

From the command line on your RPI run the following command to list all available wireless networks. You should see OpenWrt as the ESSID of one of the options.

#### $ sudo iwlist wlan0 scan

Next run the following command.

#### $ sudo raspi-config

This will launch a configuration menu. Select the Network Options item from the menu, then the Wi-fi option. On a fresh install, for regulatory purposes, you will need to specify the country in which the device is being used. Then set the SSID of the network, and the passphrase for the network.

Now run the following command to determine the IP address of the wireless device. The wireless IP address is listed after wlan0.

#### $ ifconfig

Exit out of your raspberry pi and re-login with SSH using the wireless ip address.
