import unittest

_49 = __import__('49', fromlist="Solution")


class Test(unittest.TestCase):
    def assertCustomEqual(self, first, second, msg=None):
        first = set(map(frozenset, first))
        second = set(map(frozenset, second))
        self.assertEqual(first, second, msg)

    def testcase_1(self):
        input_1 = {'strs': ["eat", "tea", "tan", "ate", "nat", "bat"]}
        output_1 = _49.Solution().groupAnagrams(**input_1)
        self.assertCustomEqual(output_1, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    def testcase_2(self):
        input_2 = {'strs': [""]}
        output_2 = _49.Solution().groupAnagrams(**input_2)
        self.assertCustomEqual(output_2, [[""]])

    def testcase_3(self):
        input_3 = {'strs': ["a"]}
        output_3 = _49.Solution().groupAnagrams(**input_3)
        self.assertCustomEqual(output_3, [["a"]])

    def testcase_4(self):
        input_4 = {'strs': ["ddddddddddg","dgggggggggg"]}
        output_4 = _49.Solution().groupAnagrams(**input_4)
        self.assertCustomEqual(output_4, [["dgggggggggg"],["ddddddddddg"]])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
