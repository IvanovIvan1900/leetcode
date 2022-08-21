from collections import defaultdict
import re
import pytest

class Solution(object):
    def check_is_substring(self, slice, dic_of_check, len_word):
        dic_of_check = dic_of_check.copy()
        for i in range(0, len(slice), len_word):
            word = slice[i:i+len_word]
            if dic_of_check.get(word, 0) > 0:
                dic_of_check[word] -= 1
            else:
                break

        return all(value == 0 for value in dic_of_check.values())

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        set_output = set()
        if len(words) > 0:
            indices_object = re.finditer(pattern='(?={0})'.format(re.escape(words[0])), string=s)
            set_all_start_index = {index.start() for index in indices_object}
            list_of_index = list(set_all_start_index)
            len_word = len(words[0])
            len_correct_substring = len(words) * len_word
            dic_of_check = defaultdict(int)
            for word in words:
                dic_of_check[word] += 1
            set_all_words = set(words)
            for curr_index in list_of_index:
                if curr_index not in set_all_start_index:
                    continue
                start_series = curr_index
                stop_series = curr_index + len_word
                # left side
                curr_start_slice = curr_index - len_word
                next_word = s[curr_start_slice:curr_start_slice + len_word]
                while curr_start_slice >= 0 and next_word in set_all_words:
                    set_all_start_index.discard(curr_start_slice)
                    start_series = curr_start_slice
                    curr_start_slice = curr_start_slice - len_word
                    next_word = s[curr_start_slice:curr_start_slice + len_word]
                # right side
                curr_start_slice = curr_index + len_word
                next_word = s[curr_start_slice:curr_start_slice + len_word]
                while curr_start_slice + len_word <= len(s) and next_word in set_all_words:
                    set_all_start_index.discard(curr_start_slice)
                    stop_series = curr_start_slice + len_word
                    curr_start_slice = curr_start_slice + len_word
                    next_word = s[curr_start_slice:curr_start_slice + len_word]
                if stop_series - start_series >= len_correct_substring:
                    for i in range(start_series, stop_series + 1 - len_correct_substring):
                        if i not in set_output and self.check_is_substring(s[i:i+len_correct_substring], dic_of_check, len_word):
                            set_output.add(i)

        return list(set_output)


class TestFindSubstring():
    solutions:Solution = Solution()

    @pytest.mark.parametrize("string,words, output_value", [
                        ("aaaaaaaaaaaaaa",["aa","aa"],[0,1,2,3,4,5,6,7,8,9,10]),
                        ("cccbcacaa",["cc","bc"],[1]),
                        ("foobarfoo",["bar","foo"],[0,3]),
                        ("sssssbarfoo",["foo","bar"],[5]),
                        ("foobarsssss",["foo","bar"],[0]),
                        ("barfoosssss",["foo","bar"],[0]),
                        ("barfoothefoobarman",["foo","bar"],[0,9]),
                        ("wordgoodgoodgoodbestword",["word","good","best","word"],[]),
                        ("barfoofoobarthefoobarman",["bar","foo","the"],[6,9,12]),
                        ("wordgoodgoodgoodbestword",["word","good","best","good"],[8]),
                        ])
    def test_find_substring(self, string:str, words:list[str], output_value:list[int])->None:
        assert sorted(output_value) == sorted(self.solutions.findSubstring(string, words))
        
    def test_big_data_v1(self):
        words = ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]
        self.solutions.findSubstring(self.get_big_strign(), words)

    def get_big_strign(self):
        return """abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                bababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab
                ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa
                babababababababababababababababababababababababab"""