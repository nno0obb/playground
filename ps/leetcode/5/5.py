import os
from typing import *


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s[0]

        for m in range(len(s)):
            for i in range(len(s)):
                l, r = m - i, m + i
                if l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        if (r-l+1) > len(ans):
                            ans = s[l:r+1]
                    else:
                        break
                else:
                    break

            for i in range(len(s)):
                l, r = m - i, (m+1) + i
                if l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        if (r-l+1) > len(ans):
                            ans = s[l:r+1]
                    else:
                        break
                else:
                    break

        return ans


if __name__ == '__main__':
    os.system('python3 5_test.py')
    # os.system('python3 5_test.py -k testcase_3')
    # os.system('python3 5_test.py -k testcase_4')  # TLE
    # os.system('python3 5_test.py -k testcase_5')  # TLE
    # os.system('python3 5_test.py -k testcase_6')
    # os.system('python3 5_test.py -k testcase_7')
