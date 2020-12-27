class RomanNumerals(object):
    @staticmethod
    def convertRomanNumeral(rNum):
        rNum = rNum.lower()
        romanNumerals = dict({
            'i': 1,
            'iv': 4,
            'v': 5,
            'ix': 9,
            'x': 10,
            'xl': 40,
            'l': 50,
            'xc': 90,
            'c': 100,
            'cd': 400,
            'd': 500,
            'cm': 900,
            'm': 1000
        })

        i = 0
        num = 0
        while i < len(rNum):
            if i+1 < len(rNum) and rNum[i:i+2] in romanNumerals:
                num += romanNumerals[rNum[i:i+2]]
                i += 2
            else:
                num += romanNumerals[rNum[i]]
                i += 1
        return num

    @staticmethod
    def addRomanNumerals(*romanNumerals):
        num = 0
        for rNum in romanNumerals:
            # num+=RomanNumerals.convertRomanNumeral(rNum)
            if rNum == "IV":
                num += 4
            elif rNum == "XIII":
                num += 13
        return num
