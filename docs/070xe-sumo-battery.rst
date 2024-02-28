Sumo Battery
===============

Overview
--------

Batteries offer a great way to power mobile robotic devices. Many are easily rechargeable and can provide large amounts of current for motors and other high current devices. There are many types of batteries defined by their chemistry. The common non-rechargable AAA or AA batteries are alkaline. Many AAA or AA rechargeable batteries are either nickel metal hydroxide (Ni-Mh) or nickel–cadmium (Ni-Cd). The batteries found in cell phones, laptops and electric cars are typically are either lithium-ion (Li-ion) or lithium-polymer (Li-Po). 

For the most part, we use Lithium Polymer (LiPo) batteries in our projects. The advantage of these sorts of batteries are that they can provide a large amount of power for their size and weight. They can be recharged quickly and can last much longer than other types of storage batteries. **DANGER:** The disadvantage is that if they are not managed carefully they can catch fire or even explode. *Explosions are bad.*

The following are important steps to take to ensure that your batteries and your circuit remain in working order

- **Never let the leads touch!** Never let the positive and negative leads of your battery touch. This is called a short circuit. These batteries can easily dump huge amounts of current and when they do so unrestricted through a small wire very bad things happen!

- **Never allow reverse polarity:** If you mistaken reverse the leads on the battery and apply the positive lead of the battery to the ground on your circuit and the negative lead to power, you circuit and board will most likely be destroyed in a sad display of smoke and melted plastic.

- **Always use polarized connectors:** It is very important to only use polarized connectors with the LiPo batteries. This will avoid the problem of reverse polarity.

- **Avoid low voltage:** It is important to make sure that the voltage in a battery never goes below factory spec. Once a lipo reaches this state is becomes unstable and can catch fire. It is also harder if not impossible to recharge. In order to ensure this does not happen, batteries should be checked every day using a LiPo tester. Ask your teacher to demonstrate testing.

- **Balance Charge:** A LiPo battery should be charged to balance charge before being used in your device. The balance charge ensures that each cell in the battery pack is charged to the identical voltage level. Ask your teacher to demonstrate balance charge on the charging device.

- **Storage Charge:** Before returning a battery to storage it should be correctly discharged to a storage state selecting the Storage Charge state on the battery charger.

Challenge
~~~~~~~~~

Construct a connector to safely power your logic and motors from a Lipo battery.  

#. Find a 7.4V 1000 mah batter from the Balanced Charged side of the blue battery bin.

#. Collect a pre-wired JST connector that mates with your battery from the JST battery lead draw in the grey cabinet.

#. Crimp a two-pin polarized connector the red and black leads at the opposite end of the JST connector. 

#. Add a right angle connector to your breadboard in line with Vin and ground on your Metro Mini or equivalent device.

#. Connect your two-pin header. Make sure it is correctly polarized and hot glue it into place.

