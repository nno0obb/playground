import unittest

_21 = __import__('21', fromlist="Solution")


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
        input_1 = {'list1': self.create_head([1, 2, 4]), 'list2': self.create_head([1, 3, 4])}
        output_1 = _21.Solution().mergeTwoLists(**input_1)
        self.assertCustomEqual(output_1, [1, 1, 2, 3, 4, 4])

    def testcase_2(self):
        input_2 = {'list1': self.create_head([]), 'list2': self.create_head([])}
        output_2 = _21.Solution().mergeTwoLists(**input_2)
        self.assertCustomEqual(output_2, [])

    def testcase_3(self):
        input_3 = {'list1': self.create_head([]), 'list2': self.create_head([0])}
        output_3 = _21.Solution().mergeTwoLists(**input_3)
        self.assertCustomEqual(output_3, [0])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
