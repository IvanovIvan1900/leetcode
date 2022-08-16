import pytest

class Solution(object):
    n = None
    array_result = None
    curr_array = None
    def recurse_calculate(self, curr_index, curr_summ, curr_n):
        if curr_index < self.n*2:
            if curr_n > 0:
                self.curr_array[curr_index] = "("
                self.recurse_calculate(curr_index+1, curr_summ+1, curr_n-1)
            if curr_summ > 0:
                self.curr_array[curr_index] = ")"
                self.recurse_calculate(curr_index+1, curr_summ-1, curr_n)
        else:
            self.array_result.append("".join(self.curr_array))

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        curr_summ = 0
        curr_index = 0
        self.array_result = []
        self.n = n
        self.curr_array = [""]*2*n
        self.recurse_calculate(curr_index, curr_summ, n)

        return self.array_result

class TestGenerateParenthesis():
    solution:Solution = Solution()

    @pytest.mark.parametrize("input_value,output_value_expected", [
                        (2, ["()()", "(())"]),
                        (1, ["()"]),
                        (3,["((()))","(()())","(())()","()(())","()()()"]),
                        ])
    def test_generate_parentheses(self, input_value:list[str], output_value_expected:str):
        assert sorted(output_value_expected) == sorted(self.solution.generateParenthesis(input_value))