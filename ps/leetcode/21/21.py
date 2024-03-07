import os
import sys
from typing import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = last = ListNode(val=-sys.maxsize)

        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                last.next, curr1 = curr1, curr1.next
            else:
                last.next, curr2 = curr2, curr2.next
            last = last.next

        while curr1:
            last.next, curr1 = curr1, curr1.next
            last = last.next
        while curr2:
            last.next, curr2 = curr2, curr2.next
            last = last.next

        return dummy.next


if __name__ == '__main__':
    os.system('python3 21_test.py')
    # os.system('python3 21_test.py -k testcase_1')
