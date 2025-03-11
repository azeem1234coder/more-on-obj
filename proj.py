class RomanConverter:
    def __init__(self, number):
        """
        Initialize the RomanConverter with an integer number.
        """
        if not isinstance(number, int):
            raise ValueError("Input must be an integer")
        if not 1 <= number <= 3999:
            raise ValueError("Input must be between 1 and 3999")
        self.number = number

    def to_roman(self):
        """
        Convert the integer value to a Roman numeral.
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_numeral = ""
        num = self.number
        
        for i in range(len(val)):
            while num >= val[i]:
                roman_numeral += syb[i]
                num -= val[i]
        
        return roman_numeral

# Example Usage
number = 2024
converter = RomanConverter(number)
print(f"The Roman numeral for {number} is {converter.to_roman()}")
