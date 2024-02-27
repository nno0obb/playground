import unittest

_819 = __import__('819', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'paragraph': "Bob hit a ball, the hit BALL flew far after it was hit.", 'banned': ["hit"]}
        output_1 = _819.Solution().mostCommonWord(**input_1)
        self.assertEqual(output_1, "ball")

    def testcase_2(self):
        input_2 = {'paragraph': "a.", 'banned': []}
        output_2 = _819.Solution().mostCommonWord(**input_2)
        self.assertEqual(output_2, "a")

    def testcase_3(self):
        input_3 = {'paragraph': "a, a, a, a, b,b,b,c, c", 'banned': ["a"]}
        output_3 = _819.Solution().mostCommonWord(**input_3)
        self.assertEqual(output_3, "b")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
