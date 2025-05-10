import unittest
from unittest.mock import patch
from wumpus import *
#from wumpus import combineNumeral

wumpusMap = {
        1: [2, 5, 8],
        2: [1, 3, 10],
        3: [2, 4, 12],
        4: [3, 5, 14],
        5: [1, 4, 6],
        6: [5, 7, 15],
        7: [6, 8, 17],
        8: [1, 7, 9],
        9: [8, 10, 18],
        10: [2, 9, 11],
        11: [10, 12, 19],
        12: [3, 11, 13],
        13: [12, 14, 20],
        14: [4, 13, 15],
        15: [6, 14, 16],
        16: [15, 17, 20],
        17: [7, 16, 18],
        18: [9, 17, 19],
        19: [11, 18, 20],
        20: [13, 16, 19]
    }

class TestWumpus(unittest.TestCase):
    @patch('builtins.input', side_effect=[2])
    @patch.object(__import__('wumpus'), 'batLogic', return_value=1)
    def test_movement(self, mock_bat, mock_input):
        result = movePlayer(1, wumpusMap, 2,2,1,4,5,)
        self.assertEqual(result, 21)

    @patch('builtins.input', side_effect=[1])
    @patch.object(__import__('wumpus'), 'batLogic', return_value=1)
    def test_movement2(self, mock_bat, mock_input):
        result = movePlayer(5,wumpusMap,2,2,1,4,5)
        self.assertEqual(result, 21)  # Fell into pit, not Wumpus

    def test_wumpus_near(self):
        result = checkHazards(5,wumpusMap,1,2,3,4,6)
        self.assertIn("You smell a wumpus", result)

    def test_hole_near(self):
        result = checkHazards(2,wumpusMap,1,6,3,4,7)
        self.assertIn("You feel a draft", result)

    @patch('builtins.input', side_effect=[3, 2, 3, 4])
    def test_kill_wumpus(self, mock_input):
        result = shootArrow(wumpusMap,1,4)
        self.assertEqual(result, 2)

    @patch('random.random', return_value=0.7)
    @patch('random.choice', return_value=5)
    def test_missed_arrow(self, mock_choice, mock_random):
        alive, wumpusPos = missedArrow(wumpusMap,5,2)
        self.assertFalse(alive)
        self.assertEqual(wumpusPos, 5)

if __name__ == '__main__':
    unittest.main()
