==========
Evil Alien
==========

Somewhere beneath you, in deepest, blackest space, works Elron, the Evil Alien. You've managed to deactivate all but his short-range weapons, but he can still make his ship invisible. You know he's somewhere within the three-dimensional grid you can see on your ship screen, but where?

You have four space bombs. Each one can be exploded at a position in the grid specified by three numbers between 0 and 9. Can you blast the Evil Elron out of space before he creeps up and captures you?


The code
========

.. literalinclude:: evil_alien.py
   :language: python


How to make the game harder
---------------------------

This program has been written so that you can easily change the difficulty by changing the size of the grid. To do this, put a different value for `s` in line 10.

If you increase the grid size you will need more space bombs to give you a fair chance of blasting Elron. Do this by changing the value of `goes` in line 14.

Puzzle corner
-------------

Can you work out how to change the program so that the computer asks you for a difficulty number which it can out into `size` instead of `size` being fixed? 
(Tip: limit the value of `size` to between 6 and 30 and use `int(size//3)` for the value of `goes` in line 14.)
