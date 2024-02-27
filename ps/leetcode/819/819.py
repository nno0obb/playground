import re
import os
from typing import *
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        counter = Counter(re.sub(r'\W', ' ', paragraph).lower().split())
        for banned_word in banned:
            if banned_word.lower() in counter:
                counter.pop(banned_word.lower())

        most_common_word, _ = counter.most_common(1).pop()
        return most_common_word


if __name__ == '__main__':
    os.system('python3 819_test.py')
