from leetcode75._1732.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 1 == sol.largestAltitude([-5,1,5,0,-7])

    def test_two(self):
        assert 0 == sol.largestAltitude([-4,-3,-2,-1,4,3,2])

    def test_three(self):
        assert 1 == sol.largestAltitude([-4,4,-3,3,-2,3,-1,1,-5,5])

