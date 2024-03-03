import os
from typing import *


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = sum(sorted(nums)[::2])
        return ans


if __name__ == '__main__':
    os.system('python3 561_test.py')
