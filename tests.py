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

  def test_sce_1_2_2(self):
    self.assertEqual(program.RomanNumerals.convertRomanNumeral("IX"), 9)

  def test_sce_1_2_3(self):
    self.assertEqual(program.RomanNumerals.convertRomanNumeral("XIV"), 14)

  def test_sce_1_3_1(self):
    self.assertEqual(program.RomanNumerals.addRomanNumerals("I"), 1)

  def test_sce_1_3_2(self):
    self.assertEqual(program.RomanNumerals.addRomanNumerals("I", "III"), 4)

if __name__ == "__main__":
    unittest.main()
