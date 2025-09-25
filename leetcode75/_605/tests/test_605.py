from leetcode75._605.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert True == sol.canPlaceFlowers([1,0,0,0,1], 1)

    def test_two(self):
        assert False == sol.canPlaceFlowers([1,0,0,0,1], 2)

    def test_three(self):
        assert True == sol.canPlaceFlowers([1,0,0,0,1,0,0,0,1], 2)

