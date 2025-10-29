from leetcode75._17.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert ["ad","ae","af","bd","be","bf","cd","ce","cf"] == sol().letterCombinations("23")

    def test_two(self):
        assert ["a","b","c"] == sol().letterCombinations('2')

    # def test_three(self):
    #     assert == sol().

