from leetcode75._746.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 15 == sol().minCostClimbingStairs([10,15,20])

    def test_two(self):
        assert 6 == sol().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])

    def test_three(self):
        assert 304 == sol().minCostClimbingStairs([101,100,1,1,1,101,100,1,100,1,101,100])

    def test_four(self):
        assert 1 == sol().minCostClimbingStairs([1000,1])
