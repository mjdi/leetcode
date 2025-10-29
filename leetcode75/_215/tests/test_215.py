from leetcode75._215.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 5 == sol().findKthLargest([3,2,1,5,6,4], 2)

    def test_two(self):
        assert 4 == sol().findKthLargest([3,2,3,1,2,4,5,5,6], 4)

