from leetcode75._1071.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert "ABC" == sol().gcdOfStrings("ABCABC", "ABC")

    def test_two(self):
        assert "AB" == sol().gcdOfStrings("ABABAB", "ABAB")

    def test_three(self):
        assert "" == sol().gcdOfStrings("LEET", "CODE")

