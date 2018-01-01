=============
Robot Missile
=============

The year is 2582 and the people of Earth are in the midst of a battle against
the Robots. A lethal Robot Missle has just landed and everyone is depending on
you to find the secret code which unlocks its defuse mechanism. If you fail,
the entire Earth Command Headquarters will be blown up.

Your computer knows what the code letter is. You must type in your guess and
it will tell you whether the code letter is earlier or later in the alphabet.
You have four chances to find the correct letter before the missile blows up.

The code
========

.. literalinclude:: robot_missile.py
   :language: python

Adding to the program
---------------------

You can make the computer print an extra message for a correct guess on the
last go. Change line 37 to read::

    print('You did it%s!' % (' (just)' if guesses == 4 else ''))

This inserts some text between "it" and the exclamation mark; the text that is
inserted is dependent on the value of `guesses` at the end of the loop.

Puzzle corner
-------------

See if you can work out how to change the program to give you more or less
changes of guessing the code letter.
