from leetcode75._238.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [24,12,8,6] == sol().productExceptSelf([1,2,3,4])

    def test_two(self):
        assert [0,0,9,0,0] == sol().productExceptSelf([-1,1,0,-3,3])

    def test_three(self):
        assert [120,-60,40,-30,24] == sol().productExceptSelf([-1,2,-3,4,-5])

