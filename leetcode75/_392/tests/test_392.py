from leetcode75._392.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert True == sol.isSubsequence("abc", "ahbgdc")

    def test_two(self):
        assert False == sol.isSubsequence("axc", "ahbgdc")
 
    def test_three(self):
        assert True == sol.isSubsequence("amz", "abcmxyz")

