from leetcode75._1657.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert True == sol().closeStrings("abc","bca")

    def test_two(self):
        assert False == sol().closeStrings("a", "aa")

    def test_three(self):
        assert True == sol().closeStrings("cabbba", "abbccc")

