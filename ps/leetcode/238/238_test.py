import unittest

_238 = __import__('238', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'nums': [1, 2, 3, 4]}
        output_1 = _238.Solution().productExceptSelf(**input_1)
        self.assertEqual(output_1, [24, 12, 8, 6])

    def testcase_2(self):
        input_2 = {'nums': [-1, 1, 0, -3, 3]}
        output_2 = _238.Solution().productExceptSelf(**input_2)
        self.assertEqual(output_2, [0, 0, 9, 0, 0])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
