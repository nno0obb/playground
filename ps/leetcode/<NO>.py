import os
from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(list(filter(lambda x: x.isalpha(), s.lower())))
        return s == s[::-1]


if __name__ == '__main__':
    os.system('python3 <NO>_test.py')
