import os
from typing import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # 1221 / 12321
        #  rs     r s

        rev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and slow:
            if rev.val != slow.val:
                return False
            rev, slow = rev.next, slow.next
        return True


if __name__ == '__main__':
    os.system('python3 234_test.py')
    # os.system('python3 234_test.py -k testcase_1')
