import unittest
import program

class Test(unittest.TestCase):
  def test_sce_1_1_1(self):
    self.assertEqual(program.RomanNumerals.addRomanNumerals(""), 0)

if __name__ == "__main__":
    unittest.main()