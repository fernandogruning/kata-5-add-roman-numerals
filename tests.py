import unittest
import program

class Test(unittest.TestCase):
  def test_sce_1_1_1(self):
    self.assertEqual(program.RomanNumerals.addRomanNumerals(""), 0)

  def test_sce_1_1_2(self):
    self.assertEqual(program.RomanNumerals.addRomanNumerals("IV"), 4)

  def test_sce_1_1_3(self):
    self.assertEqual(program.RomanNumerals.addRomanNumerals("XIII"), 13)

  def test_sce_1_2_1(self):
    self.assertEqual(program.RomanNumerals.convertRomanNumeral("I"), 1)

if __name__ == "__main__":
    unittest.main()
