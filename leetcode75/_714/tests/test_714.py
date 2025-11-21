from leetcode75._714.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 8 == sol().maxProfit([1,3,2,8,4,9], 2)

    def test_two(self):
        assert 6 == sol().maxProfit([1,3,7,5,10,3], 3)

    def test_three(self):
        assert 0 == sol().maxProfit([9,8,7,6.5], 2)

