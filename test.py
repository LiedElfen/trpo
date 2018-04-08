#!/usr/bin/env python3
import unittest
from calc import calc, calc_line

class TestCalculator(unittest.TestCase):

        def test_sum(self):
                self.assertEqual(calc_line('+ 2 2'), 4)

        def test_mul(self):
                self.assertEqual(calc_line('* 2 3'), 6)

        def test_sub(self):
                self.assertEqual(calc_line('- 5 3'), 2)

        def test_div(self):
                self.assertEqual(calc_line('/ 9 3'), 3) 

        def test_invalid(self):
                self.assertRaises(ValueError, calc_line, 'Invalid!')

        def test_extra_spaces(self):
                self.assertEqual(calc_line(' +  2  3'), 5)

if __name__=='__main__':
        unittest.main()
