from leetcode75._1456.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 3 == sol().maxVowels("abciiidef", 3)

    def test_two(self):
        assert 2 == sol().maxVowels("aeiou", 2)

    def test_three(self):
        assert 2 == sol().maxVowels("leetcode", 3)

