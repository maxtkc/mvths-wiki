Simple Switch
=============

Overview
--------

In this lesson, you will use a momentary switch to turn on and off an LED. Like all switches, a momentary switch is able to complete or disconnect a circuit with the press of a button. A momentary switch is named for the fact that it is only connected (completing the circuit) when the button is pressed or momentarily. When the button is released the circuit is disconnected. Below is a picture of a momentary switch.

Note that it has four leads (or legs). This can make it confusing to use since you only need two leads (or legs) to open and close a circuit, but which ones. This is explained below.

.. figure:: images/image89.png

   Momentary Switch

Below are two diagrams from the datasheet for the momentary switch. Note that every component you use in this shops has a datasheet. Many are only a single page but the longest are over 600 pages. In the image on the left in the small box labeled "CIRCUIT DIAGRAM" is a schematic representation of the button. That is, it does not represent a functional versus physical representation of the button. The image on the right shows a physical represenation of the button.

In the schematic diagram the leads (or legs) are numbered 1 through 4. You can also see that leads 1 and 2 are connected. There is electrically no difference between these leads. Connecting a component to lead 1 is identical to connecting a component to lead 2. The same can be said for leads 3 and 4. 

Now notice that the physical diagram on the right is also numbered 1 through 4. These numbers coorespond directly to the schematic. Leads 1 and 2 are internally connected. Leads 3 and 4 are internally connected. 

The button is normally open. That is, when the button in not pressed, there is no connection between the 3 and 4 side of the button and the 1 and 2 side of the button. 

So why do they make buttons so complicated? The purpose of the four leads is to allow them to be more securely fastened to a circuit board.

|image0|\ |image1|

Exercise:
~~~~~~~~~

#. Using your breadboard, complete the following circuit which uses a switch to turn on and off an LED. When placing your button on the breadboard make sure not to short the two sides, (1 and 2) and (3 and 4) by placing them in a connected row or column.

   .. figure:: images/image121.png 

   TEACHER CHECK \_\_\_\_\_

#. Wire the components in a different order from the circuit shown above. The LED should still light when the button is pressed.

   TEACHER CHECK \_\_\_\_\_

.. |image0| image:: images/image124.png
.. |image1| image:: images/image54.png
