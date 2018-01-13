=============
Escape!
=============

The Robots have caught you, taken your weapons and locked you up. Suddenly you remember you still have your sonar wristwatch, which can be tuned to produre sounds of any frequency. If you can only find the resonant frequency of your Robot guards, they should vibrate so much they fall apart.

You must be carefus not to use frequencies that are too low or the building will vibrate and collapse on top of you. If you go too high, you will get such a headache you will have to give up.

Can you escape the horrors of the Robot prison? (Look carefully at the program for a clue to the range of frequencies to try.)

The code
========

.. literalinclude:: escape.py
   :language: python


Puzzle corner
-------------

The three Robrt guards each have their own resonant frequency. You can't escape until you have found all three. How could you change the prograw to do this?

How to make the game harder
---------------------------

Change the number in the first "if" statement from 5 to a lower number. This means you have te get closer to the frequency to win. You can also increase the possible range of the frequency variable by changing the 100 to a higher number.
