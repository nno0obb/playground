import os
from typing import *


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l2r = height[::]
        for i in range(1, len(height)):
            l2r[i] = max(l2r[i-1], height[i])

        r2l = height[::]
        for i in range(len(height)-2, 0, -1):
            r2l[i] = max(r2l[i+1], height[i])

        ans = 0
        for i in range(1, len(height)-1):
            ans += max(0, min(l2r[i], r2l[i]) - height[i])

        return ans


if __name__ == '__main__':
    os.system('python3 42_test.py')
