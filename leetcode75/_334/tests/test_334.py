from leetcode75._334.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert True == sol.increasingTriplet([1,2,3,4,5])

    def test_two(self):
        assert False == sol.increasingTriplet([5,4,3,2,1])

    def test_three(self):
        assert True == sol.increasingTriplet([2,1,5,0,4,6])

