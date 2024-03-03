import unittest

_121 = __import__('121', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'prices': [7, 1, 5, 3, 6, 4]}
        output_1 = _121.Solution().maxProfit(**input_1)
        self.assertEqual(output_1, 5)

    def testcase_2(self):
        input_2 = {'prices': [7, 6, 4, 3, 1]}
        output_2 = _121.Solution().maxProfit(**input_2)
        self.assertEqual(output_2, 0)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
