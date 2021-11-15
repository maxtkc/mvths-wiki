Arrays
======

Overview
--------

Arrays provide a way to store multiple variables under a single variable name. This is very convenient for sets of variables that need to be accessed sequentially.

The following is an example of how to initialize an array. Similar to initializing a variable, you need to give the array a type. In the example below the array type is int. Also, as with variables, you also need to give the array a name. In the case below, the name of the array is example, but just like variables, you can give it any name you want.  The number in the square braces determines the size of the array or how many items it can hold. The array below can hold three items or more specifically three ints. Inside the curly braces are listed the items in the array.

.. code-block:: c

  int example[3] = {2, 5, 44};  //Initializes an array with three values
  
The following example shows how to retrive an item from an array. In this case the second item (item 1 counting from 0), is placed into the variable x. 
  
.. code-block:: c

  x = example[1];  //Sets x to value of the second item in the array or 5


Exercise:
~~~~~~~~~

#. Write a program that includes an array with three elements. Print the first element in the array and record the answer in your notebook.

#. Write a program that includes an array with four elements. Print th last element in the array.

#. Write a program that includes an array with four elements. Print each element of the array in order. Each number should be printed on a separate line.

#. Write a program that includes and array that holds four different numbers. Now print each element of the array in order using a 'for loop'. 

   TEACHER CHECK \_\_\_\_

#. Write a program that includes two arrays with three elements each. Compare the first element in both arrays. If they are equal, print “equal”. If they are not equal print “not equal.”

   TEACHER CHECK \_\_\_\_

#. Write a program that includes two arrays with three elements each. Compare the two arrays to determine if they are identical (i.e. they have the same elements in the same order). If they are equal, print “equal”. If they are not equal print “not equal.”

   TEACHER CHECK \_\_\_\_

#. Repeat the exercise above, but use a for loop to compare the three elements of each array.  

   TEACHER CHECK \_\_\_\_
