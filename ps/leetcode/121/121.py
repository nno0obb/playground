import os
from typing import *


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_min, ans = prices[0], 0
        for price in prices[1:]:
            ans = max(ans, price - curr_min)
            curr_min = min(curr_min, price)

        return ans


if __name__ == '__main__':
    os.system('python3 121_test.py')
    # os.system('python3 121_test.py -k testcase_1')
