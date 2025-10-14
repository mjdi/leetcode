from leetcode75._643.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 12.75 == sol().findMaxAverage([1,12,-5,-6,50,3], 4)

    def test_two(self):
        assert 5 == sol().findMaxAverage([5], 1)

    def test_three(self):
        assert (14 + 2/3) == sol().findMaxAverage([10,9,7,1,2,37,3,4,5,6,8,12], 3)
        
