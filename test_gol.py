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
import unittest
from ha1_4_gol import *


class TestLifeGame(unittest.TestCase):

    def test_boardsize(self) -> None:
        # test different board sizes and shapes
        board2 = [
            [0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
        update_board(board2)
        self.assertEqual((len(board2), len(board2[0])), (4, 5))

    def test_stilllife_test(self):
        # test behavior of still lifes
        board3 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        update_board(board3)
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(board3, expected)

    def test_oscillators(self):
        board4 = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
        update_board(board4)
        expected = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(board4, expected)

    def test_spaceship(self):
        board5 = [
            [1, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 1, 1],
            [1, 0, 0, 0],
        ]
        update_board(board5)
        expected = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ]
        self.assertEqual(board5, expected)


if __name__ == "__main__":
    unittest.main()
