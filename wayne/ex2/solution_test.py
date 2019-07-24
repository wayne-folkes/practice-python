#!/usr/bin/env python3

import unittest
import unittest.mock

solution = __import__("solution")

class TestSolution(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(solution.is_even(6))

    def test_is_not_even(self):
        self.assertFalse(solution.is_even(5))

    def test_get_number(self):
        with unittest.mock.patch('builtins.input',return_value=5):
            self.assertIsInstance(solution.get_number(),int)
            #self.assertEqual(solution.get_number(),5)

if __name__ == '__main__':
    unittest.main()