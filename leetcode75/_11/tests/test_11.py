from leetcode75._11.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 49 == sol().maxArea([1,8,6,2,5,4,8,3,7])

    def test_two(self):
        assert 1 == sol().maxArea([1,1])

    def test_three(self):
        assert 80 == sol().maxArea([1,8,6,2,5,4,8,3,7,2,4,9,1])

