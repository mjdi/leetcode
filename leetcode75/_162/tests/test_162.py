from leetcode75._162.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 2 == sol().findPeakElement([1,2,3,1])

    def test_two(self):
        assert 5 == sol().findPeakElement([1,2,1,3,5,6,4])
