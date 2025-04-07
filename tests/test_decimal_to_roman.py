import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(1000), "M")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    def test_sumas_simples(self):
        self.assertEqual(decimal_to_roman(15), "XV")
        self.assertEqual(decimal_to_roman(6), "VI")
        self.assertEqual(decimal_to_roman(20), "XX")
        self.assertEqual(decimal_to_roman(11), "XI")
        self.assertEqual(decimal_to_roman(22), "XXII")
        self.assertEqual(decimal_to_roman(35), "XXXV")
        self.assertEqual(decimal_to_roman(63), "LXIII")
        self.assertEqual(decimal_to_roman(2000), "MM")

if __name__ == '__main__':
    unittest.main()