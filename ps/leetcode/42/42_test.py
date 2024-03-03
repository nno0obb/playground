import unittest

_42 = __import__('42', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'height': [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}
        output_1 = _42.Solution().trap(**input_1)
        self.assertEqual(output_1, 6)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
