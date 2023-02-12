import unittest
from game.update_file import update_file


class TestUpdateFile(unittest.TestCase):
    def test_update_file(self):
        self.assertEqual(update_file(3, 8), 8)
        self.assertEqual(update_file(0, 4), 4)
        self.assertEqual(update_file(23, 0), 23)
        self.assertEqual(update_file(15, 15), 15)
        self.assertEqual(update_file(12, 6), 12)

        self.assertRaises(ValueError, update_file, -6, 7)
        # now using the context manager:
        with self.assertRaises(ValueError):
            update_file(9, -17)


if __name__ == '__main__':
    unittest.main()
