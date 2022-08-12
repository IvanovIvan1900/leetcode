import pytest

class Solution(object):
    dic_num_to_let = {
        "2":["a", "b", "c"],
        "3":["d", "e", "f"],
        "4":["g", "h", "i"],
        "5":["j", "k", "l"],
        "6":["m", "n", "o"],
        "7":["p", "q", "r", "s"],
        "8":["t", "u", "v"],
        "9":["w", "x", "y", "z"],
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        list_of_symbol = [self.dic_num_to_let.get(dig) for dig in digits]
        list_of_index = [0]*len(list_of_symbol)
        list_of_result = []
        working = len(list_of_symbol)>0
        while working:
            list_of_result.append("".join([list_of_symbol[index][symbol_index] for index, symbol_index in enumerate(list_of_index)]))

            for i in range(len(list_of_index)-1, -1, -1):
                list_of_index[i] += 1
                if list_of_index[i] < len(list_of_symbol[i]):
                    break
                else:
                    working = (i > 0)
                list_of_index[i] = 0
                    
        return list_of_result

class TestLetterCombination():
    solution = Solution()

    @pytest.mark.parametrize("inpout_value, output_value", [
                ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]), 
                ("", []), 
                ("2", ["a","b","c"]) ])
    def test_solution(self, inpout_value:str, output_value:list[str]):
        assert output_value == self.solution.letterCombinations(inpout_value)
