from leetcode75._394.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert "aaabcbc" == sol.decodeString("3[a]2[bc]")

    def test_two(self):
        assert "accaccacc" == sol.decodeString("3[a2[c]]")

    def test_three(self):
        assert "abcabccdcdcdef" == sol.decodeString("2[abc]3[cd]ef")

