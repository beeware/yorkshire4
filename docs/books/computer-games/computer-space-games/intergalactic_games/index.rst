===================
Intergalactic Games
===================

There's fierce competition among the world's TV companies for exclusive coverage of the First Intergalactic Games. Everything depends on which company wins the race to put satellite into orbit at the right height.
You are the engineer in charge of the launch for New Century TV. The crucial decisions about the angle and speed of the launching rocket rests on your shoulders. Can you do it?


The code
========

.. literalinclude:: intergalactic_games.py
   :language: python


Adding to the program
---------------------

These changes will make the computer give you bonus points depending on how quickly you make a successful launch.

After line 41, insert::

        if guesses:
            bonus = 1000 * guesses
            print("You've earned a bonus of", bonus, "credits")


Puzzle corner
-------------

Can you change the program so that, if you win, it automatically goes back for another game, adding the bonus you've already earned to any new bonus?
See how long you can play before and NCTV fires you.
