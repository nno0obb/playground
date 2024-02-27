import os
from typing import *
from collections import defaultdict, Counter


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped_anagrams = defaultdict(list)
        for anagram in strs:
            grouped_anagrams[''.join(sorted(anagram))].append(anagram)

        return list(grouped_anagrams.values())


if __name__ == '__main__':
    os.system('python3 49_test.py')
