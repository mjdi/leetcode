from leetcode75._216.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [[1,2,4]] == sol().combinationSum3(3, 7)

    def test_two(self):
        assert [[1,2,6],[1,3,5],[2,3,4]] == sol().combinationSum3(3, 9)

    def test_three(self):
        assert [] == sol().combinationSum3(4, 1)

    def test_four(self):
        assert [[1,2,3,4,5,6,7,8,9]] == sol().combinationSum3(9, 45)
