from leetcode75._62.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 28 == sol().uniquePaths(3,7)

    def test_two(self):
        assert 3 == sol().uniquePaths(3,2)

    def test_three(self):
        assert 70 == sol().uniquePaths(5,5)
