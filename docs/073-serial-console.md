# Serial Console

## Overview

There are a number of ways to connect to the serial console from the command line. Five options are detailed [here](https://www.google.com/url?q=https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console/&sa=D&ust=1587613174365000). The one I will detail is screen which offers a simple barebones connection. For example, if you wanted to connect to the port ttyACM0 at a baudrate of 57600 (see above for determining which port is available) you would use the following command. If you do not include a baudrate the program defaults to 9600.

#### $ screen /dev/ttyACM0 57600

In order to end a screen session you would use ctrl-a and d for detach.

  
In order to log a screen session use the -L flag. This will create a log file.
