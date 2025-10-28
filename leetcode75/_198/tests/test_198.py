from leetcode75._198.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 4 == sol().rob([1,2,3,1])

    def test_two(self):
        assert 12 == sol().rob([2,7,9,3,1])

    def test_three(self):
        assert 71 == sol().rob([7,2,20,4,4,30,30,1,10])

    def test_four(self):
        assert 4 == sol().rob([2,1,1,2])

    def test_five(self):
        assert 12 == sol().rob([3,1,3,5,3,1,3])

    def test_six(self):
        assert 8 == sol().rob([1,2,3,1,3,2,1])