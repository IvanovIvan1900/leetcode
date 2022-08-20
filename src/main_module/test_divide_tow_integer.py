import pytest

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        output = 0
        output_is_positiv = (dividend >= 0) == (divisor >= 0)
        output_max = 2147483647+(0 if output_is_positiv else 1)
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        if dividend == 0:
            output = 0
        elif divisor == 1:
            output = dividend
        else:
            remains_dividend = dividend
            curr_index_divisors = 0
            array_divisors_step = [divisor]
            dict_divisors = {divisor: 1}
            while remains_dividend >= divisor:
                if remains_dividend > array_divisors_step[curr_index_divisors]:
                    remains_dividend = remains_dividend - array_divisors_step[curr_index_divisors]
                    output = output + dict_divisors[array_divisors_step[curr_index_divisors]]
                    dict_divisors[array_divisors_step[curr_index_divisors]+array_divisors_step[curr_index_divisors]] = dict_divisors[array_divisors_step[curr_index_divisors]] + dict_divisors[array_divisors_step[curr_index_divisors]]
                    array_divisors_step.append(array_divisors_step[curr_index_divisors]+array_divisors_step[curr_index_divisors])
                    curr_index_divisors += 1
                else:
                    curr_index_divisors -= 1
                    while array_divisors_step[curr_index_divisors] > remains_dividend:
                        curr_index_divisors -= 1
                    remains_dividend =  remains_dividend - array_divisors_step[curr_index_divisors]
                    output = output + dict_divisors[array_divisors_step[curr_index_divisors]]
        output = min(output_max, output)
        if not output_is_positiv:
            output = -output

        return output

class Testdivide():
    solutions:Solution = Solution()
    @pytest.mark.parametrize("dividend, divisor, output_value", [
                        (10,3,3),
                        (7,-3,-2),
                        (100,3,33),
                        (20, 2, 10),
                        (0, -1, 0),
                        (-2147483648, -1, 2147483647),
                        (-2147483648, 1, -2147483648),
                        ])
    def test_divide(self, dividend:int, divisor:int, output_value:int)->None:
        assert output_value == self.solutions.divide(dividend, divisor)