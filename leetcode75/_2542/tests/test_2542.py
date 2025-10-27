from leetcode75._2542.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 12 == sol().maxScore([1,3,3,2], [2,1,3,4], 3)

    def test_two(self):
        assert 30 == sol().maxScore([4,2,3,1,1], [7,5,10,9,6], 1)

    def test_three(self):
        assert 600 == sol().maxScore([100,1,1,50,50,50], [3,1,1,5,5,4], 3)

