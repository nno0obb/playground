import os
from typing import *


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        ans = []
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]:
                continue

            m, r = l+1, len(nums)-1

            while m < r:
                _sum = nums[m] + nums[r]
                if _sum == -nums[l]:
                    ans.append([nums[l], nums[m], nums[r]])

                    while m < r and nums[m] == nums[m+1]:
                        m += 1
                    m += 1
                    while m < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif _sum < -nums[l]:
                    m += 1
                elif _sum > -nums[l]:
                    r -= 1
                else:
                    raise RuntimeError()

        return ans


if __name__ == '__main__':
    os.system('python3 15_test.py')
