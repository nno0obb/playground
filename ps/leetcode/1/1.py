import os
from typing import *


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums = list(zip(nums, range(len(nums))))
        nums.sort()
        l, r, ans = 0, len(nums) - 1, -1
        while l < r:
            _sum = nums[l][0] + nums[r][0]

            if _sum == target:
                ans = [nums[l][1], nums[r][1]]
                break
            elif _sum < target:
                l += 1
            else:
                r -= 1
        if ans == -1:
            raise RuntimeError()

        return ans


if __name__ == '__main__':
    os.system('python3 1_test.py')
    # os.system('python3 1_test.py -k testcase_4')  # TLE
