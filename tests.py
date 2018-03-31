import unittest
import model

class TestExample(unittest.TestCase):

    def test_example(self):
        self.assertTrue(True)

class TestModel(unittest.TestCase):
    def setUp(self):
        self.board_one = model.Board()

    def test_try_make_move(self):
        self.assertTrue(self.board_one.try_make_move(1, 0, 0))
        self.assertFalse(self.board_one.try_make_move(2, 0, 0))
        self.assertTrue(self.board_one.try_make_move(1, 2, 2))
        self.assertFalse(self.board_one.try_make_move(1, 3, 3))

    def test_get_board(self):
        self.board_one.try_make_move(1, 0, 0)
        self.board_one.try_make_move(2, 1, 0)
        result = [[1, 0, 0], [2, 0, 0], [0]*3] == self.board_one.get_board()
        self.assertTrue(result)

    def test_check_win(self):
        self.board_one.try_make_move(1, 0, 0)
        self.board_one.try_make_move(2, 1, 0)
        self.board_one.try_make_move(1, 1, 1)
        self.board_one.try_make_move(2, 2, 0)
        self.board_one.try_make_move(1, 2, 2)
        self.board_one.try_make_move(2, 0, 2)
        self.assertTrue(self.board_one.check_win(1))
        self.assertFalse(self.board_one.check_win(2))

    def test_check_draw(self):
        self.board_one.try_make_move(1, 0, 0)
        self.board_one.try_make_move(2, 0, 1)
        self.board_one.try_make_move(1, 1, 1)
        self.board_one.try_make_move(2, 0, 2)
        self.board_one.try_make_move(1, 1, 2)
        self.board_one.try_make_move(2, 1, 0)
        self.board_one.try_make_move(1, 2, 0)
        self.board_one.try_make_move(2, 2, 2)
        self.assertFalse(self.board_one.check_draw())
        self.board_one.try_make_move(1, 2, 1)
        self.assertTrue(self.board_one.check_draw())

    def test_travis(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()



