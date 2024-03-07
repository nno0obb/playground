import unittest

_206 = __import__('206', fromlist="Solution")


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

    def assertCustomEqual(self, first, second, msg=None):
        curr_first = first
        curr_second = self.create_head(second)
        while curr_first and curr_second:
            self.assertEqual(curr_first.val, curr_second.val)
            curr_first, curr_second = curr_first.next, curr_second.next

    def testcase_1(self):
        input_1 = {'head': self.create_head([1, 2, 3, 4, 5])}
        output_1 = _206.Solution().reverseList(**input_1)
        self.assertCustomEqual(output_1, [5, 4, 3, 2, 1])

    def testcase_2(self):
        input_2 = {'head': self.create_head([1, 2])}
        output_2 = _206.Solution().reverseList(**input_2)
        self.assertCustomEqual(output_2, [2, 1])

    def testcase_3(self):
        input_3 = {'head': self.create_head([])}
        output_3 = _206.Solution().reverseList(**input_3)
        self.assertCustomEqual(output_3, [])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
