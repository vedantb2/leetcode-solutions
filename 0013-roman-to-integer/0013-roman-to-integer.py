class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev_value = 0
        for numeral in reversed(s):
            value = roman_dict[numeral]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total