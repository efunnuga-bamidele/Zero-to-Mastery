import unittest
import guessNumber

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = guessNumber.runGuess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        answer = 5
        guess = 0
        result = guessNumber.runGuess(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        answer = 5
        guess = 11
        result = guessNumber.runGuess(guess, answer)
        self.assertFalse(result)
    
    def test_input_wrong_type(self):
        result = guessNumber.runGuess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()