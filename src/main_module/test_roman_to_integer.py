import pytest


class Solution(object):
    dic_sym_to_in = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
    div_preced = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_index = 0
        int_value = 0
        while curr_index < len(s):
            curr_int_value = None
            if curr_index < (len(s)-1):
                curr_int_value = self.div_preced.get(s[curr_index:curr_index+2], None)
            if curr_int_value is None:
                curr_int_value = self.dic_sym_to_in.get(s[curr_index:curr_index+1], 0)
                curr_index += 1
            else:
                curr_index += 2

            int_value += curr_int_value

        return int_value

class TestRomanToInteger():
    solution:Solution = Solution()
    
    @pytest.mark.parametrize("roman_value,int_value", [("III", 3), ("LVIII", 58),("MCMXCIV", 1994),("IX", 9), ("MDCCCLXXXIV", 1884)])
    def test_roman_to_int(self, roman_value:str, int_value:int):
        assert self.solution.romanToInt(roman_value) == int_value

