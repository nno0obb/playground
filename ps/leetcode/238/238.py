import os
from typing import *


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l2r = nums[::]
        for i in range(1, len(nums)):
            l2r[i] *= l2r[i-1]
        r2l = nums[::]
        for i in range(len(nums)-2, 0, -1):
            r2l[i] *= r2l[i+1]

        ans = [-1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = r2l[i+1]
            elif i == len(nums)-1:
                ans[i] = l2r[i-1]
            else:
                ans[i] = l2r[i-1] * r2l[i+1]

        return ans


if __name__ == '__main__':
    os.system('python3 238_test.py')
    # os.system('python3 238_test.py -k testcase_1')
