Switch State
=========

Overview
--------

A switch statement in C is an alternative from of the a conditional i.e. *if then*. Switch serves the same purpose as *if then* but in a format that is sometimes more readable. Often code built around a switch statement is called a state machine because the the switch statement allows you to switch between different states in your code.


.. code-block:: C

   #define STATE_ONE 0
   #define STATE_TWO 1

   int state;

   void loop() {
   
      switch(state) {
      
      case STATE_ONE:
        // Code for first state goes here
      break();
      case STATE_TWO:
        // Code for second state goes here
      break();
      }

}
