import unittest
import guess_the_number


game = guess_the_number.GuessTheNumber()


class TestGuessTheNumber(unittest.TestCase):

    def test_random_number_is_int(self):
        random_number = game.random_number
        self.assertTrue(isinstance(random_number, int))

    def test_random_number_is_in_range(self):
        random_number = game.random_number
        self.assertTrue(0 <= random_number <= 101)


if __name__ == "__main__":
    unittest.main()
