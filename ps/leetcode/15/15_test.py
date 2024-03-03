import unittest

_15 = __import__('15', fromlist="Solution")


class Test(unittest.TestCase):
    def assertCustomEqual(self, first, second, msg=None):
        first = set(map(lambda x: tuple(sorted(x)), first))
        second = set(map(lambda x: tuple(sorted(x)), second))
        self.assertEqual(first, second, msg)

    def testcase_1(self):
        input_1 = {'nums': [-1, 0, 1, 2, -1, -4]}
        output_1 = _15.Solution().threeSum(**input_1)
        self.assertCustomEqual(output_1, [[-1, -1, 2], [-1, 0, 1]])

    def testcase_2(self):
        input_2 = {'nums': [0, 1, 1]}
        output_2 = _15.Solution().threeSum(**input_2)
        self.assertCustomEqual(output_2, [])

    def testcase_3(self):
        input_3 = {'nums': [0, 0, 0]}
        output_3 = _15.Solution().threeSum(**input_3)
        self.assertCustomEqual(output_3, [[0, 0, 0]])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
