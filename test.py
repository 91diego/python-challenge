import unittest
import main

class unit_test(unittest.TestCase):

    def negativeNumbers(self):
        result = main.negativeNumbers(-1)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()