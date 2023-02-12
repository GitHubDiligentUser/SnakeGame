import unittest
from game.moving_snake import move_body_parts


class TestMovingSnake(unittest.TestCase):
    def test_move_body_parts(self):
        self.assertEqual(move_body_parts('down', 50, 30), 80)  # add assertion here
        self.assertEqual(move_body_parts('up', 140, 3), 137)
        self.assertEqual(move_body_parts('left', 5.0, 3.0), 2.0)
        self.assertEqual(move_body_parts('right', 140, 3), 143)


if __name__ == '__main__':
    unittest.main()
