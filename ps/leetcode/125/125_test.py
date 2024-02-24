import unittest

_125 = __import__('125', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'s': "A man, a plan, a canal: Panama"}
        output_1 = _125.Solution().isPalindrome(**input_1)
        self.assertEqual(output_1, True)

    def testcase_2(self):
        input_2 = {'s': "race a car"}
        output_2 = _125.Solution().isPalindrome(**input_2)
        self.assertEqual(output_2, False)

    def testcase_3(self):
        input_3 = {'s': " "}
        output_3 = _125.Solution().isPalindrome(**input_3)
        self.assertEqual(output_3, True)

    def testcase_4(self):
        input_4 = {'s': "0P"}
        output_4 = _125.Solution().isPalindrome(**input_4)
        self.assertEqual(output_4, False)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
