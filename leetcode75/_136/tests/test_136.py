from leetcode75._136.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 1 == sol().singleNumber([2,2,1])

    def test_two(self):
        assert 4 == sol().singleNumber([4,1,2,1,2])

    def test_three(self):
        assert 1 == sol().singleNumber([1])

