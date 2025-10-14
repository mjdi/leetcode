from leetcode75._1679.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 2 == sol().maxOperations([1,2,3,4], 5)

    def test_two(self):
        assert 1 == sol().maxOperations([3,1,3,4,3], 6)

    def test_three(self):
        assert 3 == sol().maxOperations([6,1,3,6,4,5,2,6], 7)

