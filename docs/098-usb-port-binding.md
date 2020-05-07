# Ports

What ports are in use? Test by plugging and unplugging the USB device.

#### $ ls /dev/tty\*

# Killing a Process

In order to determine what process is using a tty port you run the command.

#### $ ps -aux |grep tty

This will list the process that is using the tty port. If the owner of the process is root, you must kill the process as root.

# Port Permissions

It is possible that you need to remove binding to a USB port. The following is helpful if you have USB1 and USB0 does not show up.

Run

$ ls /sys/bus/usb/drivers/  

To see what drivers you have. It is likely that CP210x is the one that is working

$ tree /sys/bus/usb/drivers/CP210x/ with show the device innformation

####     /sys/bus/usb/drivers/ub/

####     |-- 1-1:1.0 -\> ../../../../devices/pci0000:00/0000:00:1d.7/usb1/1-1/1-1:1.0

####     |-- bind

####     |-- module -\> ../../../../module/ub

####     \`-- unbind

In order to unbind a device from a driver, simply write the bus id of the device to the unbind file:

YOU WILL NEED TO DO THIS AS ROOT

PAY REEL ABI

   echo -n "1-1:1.0" \> /sys/bus/usb/drivers/ub/unbind

and the device will no longer be bound to the driver:

   $ tree /sys/bus/usb/drivers/ub/

    /sys/bus/usb/drivers/ub/

    |-- bind

    |-- module -\> ../../../../module/ub

    \`-- unbind

Killing jobs.,

If stopped jobs on ttymidi a kill will not kill you need to use
