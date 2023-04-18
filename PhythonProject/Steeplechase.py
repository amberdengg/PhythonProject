"""
File: Steeplechase.py
Name: Amber Deng
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()

    # move()
    # jump()
    # move()
    # jump()
    # move()
    # jump()
    # jump()
    # jump()
    # move()
    # jump()
    # jump()

def jump():
    """
    Pre-condition:Karel is on the left,facing East
    Post-condition:Karel is on the right
    """
    up()
    cross()
    down()

def up():
    """
    Pre-condition:Karel is on the left,facing East
    Post-condition:Karel is at the upper left,facing North.
    Comment/Un-comment:command+/
    """
    turn_left()
    #Karel is facing North, wall is an the right
    while not right_is_clear():
        move()
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()

def cross():
    """
    pre-condition:Karel is at the upper left,facing North.
    post-condition:Karel is at the upper right,facing North.
    """
    turn_right()
    move()
    turn_right()

def down():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
