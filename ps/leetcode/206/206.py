import os
from typing import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev, curr = None, head
        while curr:
            rev, rev.next, curr = curr, rev, curr.next
        return rev


if __name__ == '__main__':
    os.system('python3 206_test.py')
