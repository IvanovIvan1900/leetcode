from typing import List
import pytest

class Solution_not_optimal(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        list_of_prefix = []
        for n in range(len(strs[0])):
            curr_symb = strs[0][n]
            for elem in strs:
                if len(elem) < n + 1 or elem[n] != curr_symb:
                    return ''.join(list_of_prefix)
            list_of_prefix.append(curr_symb)

        return ''.join(list_of_prefix)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ""
        len_min_str = min(len(elem) for elem in strs)
        if not len_min_str:
            return ""

        if not self.check_prefix(strs, 0):
            return ""

        index_from = 0
        index_to = len_min_str
        while True:
            index_test = index_from+int((index_to - index_from)/2)
            if self.check_prefix(strs, index_test):
                index_from = index_test
            else:
                index_to = index_test

            if (index_to-index_from) < 2:
                if self.check_prefix(strs,index_to):
                    return strs[0][:index_to]
                else:
                    return strs[0][:index_from]
        
    def check_prefix(self, strs, to):
        etalon_pref = strs[0][:to]
        return all(elem[:to]==etalon_pref for elem in strs)
        

class TestCommonPrefix():
    solution:Solution = Solution()

    @pytest.mark.parametrize("input_value,output_value_expected", [([""],""),(["flower","flow","flight"],"fl"), (["dog","racecar","car"],""), (["abcd","abcde","ab"],"ab")])
    def test_commont_prefix(self, input_value:List[str], output_value_expected:str):
        assert output_value_expected == self.solution.longestCommonPrefix(input_value)