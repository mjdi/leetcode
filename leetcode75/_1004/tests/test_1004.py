from leetcode75._1004.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 6 == sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)

    def test_two(self):
        assert 10 == sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)

    def test_three(self):
        assert 11 == sol.longestOnes([1,1,1,1,1,0,1,1,1,1,0], 2)

