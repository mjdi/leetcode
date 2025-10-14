from leetcode75._345.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert "AceCreIm" == sol().reverseVowels("IceCreAm")

    def test_two(self):
        assert "leotcede" == sol().reverseVowels("leetcode")

    def test_three(self):
        assert "Marces Diumand" == sol().reverseVowels("Marcus Diemand")

