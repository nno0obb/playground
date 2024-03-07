import unittest

_234 = __import__('234', fromlist="Solution")


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Test(unittest.TestCase):
    @staticmethod
    def create_head(lst):
        head, curr_node, prev_node = None, None, None
        for val in lst:
            curr_node = ListNode(val=val)
            if prev_node:
                prev_node.next = curr_node
            else:
                head = curr_node
            prev_node = curr_node
        return head

    def testcase_1(self):
        input_1 = {'head': self.create_head([1, 2, 2, 1])}
        output_1 = _234.Solution().isPalindrome(**input_1)
        self.assertEqual(output_1, True)

    def testcase_2(self):
        input_2 = {'head': self.create_head([1, 2])}
        output_2 = _234.Solution().isPalindrome(**input_2)
        self.assertEqual(output_2, False)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
