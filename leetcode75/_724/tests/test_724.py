from leetcode75._724.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 3 == sol.pivotIndex([1,7,3,6,5,6])

    def test_two(self):
        assert -1 == sol.pivotIndex([1,2,3])

    def test_three(self):
        assert 0 == sol.pivotIndex([2,1,-1])

