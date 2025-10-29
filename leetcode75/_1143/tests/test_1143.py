from leetcode75._1143.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 3 == sol().longestCommonSubsequence("abcde","ace")

    def test_two(self):
        assert 3 == sol().longestCommonSubsequence("abc", "abc")

    def test_three(self):
        assert 0 == sol().longestCommonSubsequence("abc", "def")
    
    def test_four(self):
        assert 2 == sol().longestCommonSubsequence("ezupkr", "ubmrapg")

    def test_five(self):
        assert 14 == sol().longestCommonSubsequence(
            "dknkdizqxkdczafixidorgfcnkrirmhmzqbcfuvojsxwraxe",
            "dulixqfgvipenkfubgtyxujixspoxmhgvahqdmzmlyhajerqz"
            )
