"""Homework: Unittests for Game of Life.

Notes: The goal of this exercise is to write unit tests for the Game of Life
    update_board function. Write tests to check for the correctness of
    different aspects of the function. You should at least check for:

    - different board sizes and shapes
    - behavior of still lifes
    - behavior of oscillators
    - behavior of spaceships
    - objects near each edge

    Hint: If present, remove time.sleep calls from code to make testing faster.
"""

# import your update_board function here
from ctypes import sizeof
from turtle import up
from ha1_4_gol import update_board
def boardsize_test_gol() -> None:
    #test different board sizes and shapes
    board2 = [
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ]
    res1=update_board(board2)
    assert res1.shape==(4,5)
def stilllife_test_gol():
    #test behavior of still lifes
    board3 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    res2=update_board(board3)
    assert res2==[
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
def oscillators_test_fgol():
    board4 = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    res2=update_board(board4)
    assert res2==[
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
def spaceship_test_gol():
    board5 = [
        [1, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
    ]
    res3=update_board(board5)
    assert res3==[
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
    ]


