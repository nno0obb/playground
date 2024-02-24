import unittest

_937 = __import__('937', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'logs': ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]}
        output_1 = _937.Solution().reorderLogFiles(**input_1)
        self.assertEqual(output_1, ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"])

    def testcase_2(self):
        input_2 = {'logs': ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]}
        output_2 = _937.Solution().reorderLogFiles(**input_2)
        self.assertEqual(output_2, ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
