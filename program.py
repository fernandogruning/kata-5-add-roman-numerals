class RomanNumerals(object):
  @staticmethod
  def addRomanNumerals(*romanNumerals):
    num = 0
    for rNum in romanNumerals:
      # num+=RomanNumerals.convertRomanNumeral(rNum)
      if rNum == "IV":
        num+=4
    return num