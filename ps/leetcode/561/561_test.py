import unittest

_561 = __import__('561', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'nums': [1, 4, 3, 2]}
        output_1 = _561.Solution().arrayPairSum(**input_1)
        self.assertEqual(output_1, 4)

    def testcase_2(self):
        input_2 = {'nums': [6, 2, 6, 5, 1, 2]}
        output_2 = _561.Solution().arrayPairSum(**input_2)
        self.assertEqual(output_2, 9)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
