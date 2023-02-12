import unittest
from game.new_way import move


class TestNewWay(unittest.TestCase):
    def test_move(self):
        self.assertEqual(move('left', 'right'), 'right')
        self.assertEqual(move('left', 'left'), 'left')
        self.assertEqual(move('up', 'right'), 'up')
        self.assertEqual(move('down', 'left'), 'down')


if __name__ == '__main__':
    unittest.main()
