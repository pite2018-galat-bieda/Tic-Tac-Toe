import unittest
import model


class TestExample(unittest.TestCase):

    def test_example(self):
        self.assertTrue(True)

class TestModel(unittest.TestCase):
    def test_try_make_move(self):
        a = model.Board()
        self.assertTrue(a.try_make_move(1, 0, 0))
        self.assertFalse(a.try_make_move(2, 0, 0))
        self.assertTrue(a.try_make_move(1, 2, 2))
        self.assertFalse(a.try_make_move(1, 3, 3))
    def test_get_board(self):
        a = model.Board()
        a.try_make_move(1, 0, 0)
        a.try_make_move(2, 1, 0)
        result = [[1, 0, 0], [2, 0, 0], [0]*3] == a.get_board()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
