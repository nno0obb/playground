import unittest

_344 = __import__('344', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'s': ["h", "e", "l", "l", "o"]}
        _ = _344.Solution().reverseString(**input_1)
        self.assertEqual(input_1['s'], ["o", "l", "l", "e", "h"])

    def testcase_2(self):
        input_2 = {'s': ["H", "a", "n", "n", "a", "h"]}
        _ = _344.Solution().reverseString(**input_2)
        self.assertEqual(input_2['s'], ["h", "a", "n", "n", "a", "H"])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
