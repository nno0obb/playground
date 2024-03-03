import unittest

_5 = __import__('5', fromlist="Solution")


class Test(unittest.TestCase):
    def testcase_1(self):
        input_1 = {'s': "babad"}
        output_1 = _5.Solution().longestPalindrome(**input_1)
        self.assertEqual(output_1, "bab")

    def testcase_2(self):
        input_2 = {'s': "cbbd"}
        output_2 = _5.Solution().longestPalindrome(**input_2)
        self.assertEqual(output_2, "bb")

    def testcase_3(self):
        input_3 = {'s': "bb"}
        output_3 = _5.Solution().longestPalindrome(**input_3)
        self.assertEqual(output_3, "bb")

    def testcase_4(self):  # TLE
        input_4 = {'s': "cstgvkbrxacmpxdxxktktvpdzcuxmnhvuxdgsmskgeeawzeikhtmhdvnccbrgifpzmiuytfmeyfoxsntrdtxeuxcqsndexbgfxnthqwveujqzemloooyddparbjcuiwpopjwvvmwblsamkhjhlnoxinkpsempexmipifsfwzxbetgvfnkngzxcpizwctpdlpngjpyovmjllxfiwktghkxvyelwjwdztujmunijfsfdvmhgqhlpouewgyznphlmccjmqaqncwbeqheohibafqfunfywmrvqvjygjwqoclijwkcfiuaiymeagdbwyejnvtosxylptbtyoahfzfmwzrkhzdamknleroffmsqcaryibamgdpcumlhrblypddzhaxfeztokgogzgvpfvlmetiwsamhdidmvxavleryfyakendwrbslcavlqkerrnvpuzhdgwzuyorxzbkzhxhpbvkflgxouvaavxrdzsjlgrmogzvlhhdidldsxqhrqlryaanffhxnutcycnczuedtrwcnfiqrtoafvdfnfhxhyjivzalozrbrajboecfyalisxxanduzraqdrbzsbkobaieqpzcawrunxucypqyjnmrlrlivrrwwhdpekeelsphhunzbhkkejvqfopjsuholutgmtnleqdrntbqgrobnuhqpdkbjtikijkdiwqvnxgajaaqgswrdamzv"}
        output_4 = _5.Solution().longestPalindrome(**input_4)
        self.assertEqual(output_4, "vaav")

    def testcase_5(self):  # TLE
        input_5 = {'s': "tktneonoubkxgfhybavrfnetlxgtkelsoeeuznssntcleenqgiboexflfvlfiapqjbcwyenmfnmxcbcjscucqhwuqfzvvkdxrtxzhjdvsjawcwffoglhkxvyxaninlswyjcfvdwfkqheidwprtjaaqzqgloctafkuasubqqeacdpmtfzokccmnslnklxyvfitbfbdjrlzhkhnturfkimghcnngvdhbehewzzyfsbsactkrfabkhaavryubckkrqbqcbenqpeykyawzkctswaczbjtzeyteftsjklrtchxggsslscypkuilhbitsjwzsvwmqahxkmghigdtuqehjkqswchkrolcloxnkqocyjeorkwjmbevwijmqfhtmolspqcqshafjuxcheckguzxvapfivznkzdkzwnvlquzrbkhvmpdclrettjrxinbbvlwtsyepestvwjfiekjaqphfrhiifrplokslzaxmlwafrrfawlmxazlskolprfiihrfhpqajkeifjwvtsepeystwlvbbnixrjtterlcdpmvhkbrzuqlvnwzkdzknzvifpavxzugkcehcxujfahsqcqpslomthfqmjiwvebmjwkroejycoqknxolclorkhcwsqkjhequtdgihgmkxhaqmwvszwjstibhliukpycslssggxhctrlkjstfetyeztjbzcawstckzwaykyepqnebcqbqrkkcbuyrvaahkbafrktcasbsfyzzwehebhdvgnnchgmikfrutnhkhzlrjdbfbtifvyxlknlsnmcckozftmpdcaeqqbusaukfatcolgqzqaajtrpwdiehqkfwdvfcjywslninaxyvxkhlgoffwcwajsvdjhzxtrxdkvvzfquwhqcucsjcbcxmnfmneywcbjqpaiflvflfxeobigqneelctnssnzueeoslektgxltenfrvabyhfgxkbuonoentkt"}
        output_5 = _5.Solution().longestPalindrome(**input_5)
        self.assertEqual(output_5, "tktneonoubkxgfhybavrfnetlxgtkelsoeeuznssntcleenqgiboexflfvlfiapqjbcwyenmfnmxcbcjscucqhwuqfzvvkdxrtxzhjdvsjawcwffoglhkxvyxaninlswyjcfvdwfkqheidwprtjaaqzqgloctafkuasubqqeacdpmtfzokccmnslnklxyvfitbfbdjrlzhkhnturfkimghcnngvdhbehewzzyfsbsactkrfabkhaavryubckkrqbqcbenqpeykyawzkctswaczbjtzeyteftsjklrtchxggsslscypkuilhbitsjwzsvwmqahxkmghigdtuqehjkqswchkrolcloxnkqocyjeorkwjmbevwijmqfhtmolspqcqshafjuxcheckguzxvapfivznkzdkzwnvlquzrbkhvmpdclrettjrxinbbvlwtsyepestvwjfiekjaqphfrhiifrplokslzaxmlwafrrfawlmxazlskolprfiihrfhpqajkeifjwvtsepeystwlvbbnixrjtterlcdpmvhkbrzuqlvnwzkdzknzvifpavxzugkcehcxujfahsqcqpslomthfqmjiwvebmjwkroejycoqknxolclorkhcwsqkjhequtdgihgmkxhaqmwvszwjstibhliukpycslssggxhctrlkjstfetyeztjbzcawstckzwaykyepqnebcqbqrkkcbuyrvaahkbafrktcasbsfyzzwehebhdvgnnchgmikfrutnhkhzlrjdbfbtifvyxlknlsnmcckozftmpdcaeqqbusaukfatcolgqzqaajtrpwdiehqkfwdvfcjywslninaxyvxkhlgoffwcwajsvdjhzxtrxdkvvzfquwhqcucsjcbcxmnfmneywcbjqpaiflvflfxeobigqneelctnssnzueeoslektgxltenfrvabyhfgxkbuonoentkt")

    def testcase_6(self):
        input_6 = {'s': "ccc"}
        output_6 = _5.Solution().longestPalindrome(**input_6)
        self.assertEqual(output_6, "ccc")

    def testcase_7(self):
        input_7 = {'s': "aaaa"}
        output_7 = _5.Solution().longestPalindrome(**input_7)
        self.assertEqual(output_7, "aaaa")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'testcase'
    unittest.main(testLoader=loader)
