from leetcode75._151.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert "blue is sky the" == sol.reverseWords("the sky is blue")

    def test_two(self):
        assert "world hello" == sol.reverseWords("hello world")

    def test_three(self):
        assert "example good a" == sol.reverseWords("a good   example")

