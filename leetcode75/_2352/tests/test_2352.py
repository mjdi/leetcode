from leetcode75._2352.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 1 == sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]])

    def test_two(self):
        assert 3 == sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])

    def test_three(self):
        assert 3 == sol.equalPairs([[1,2,3],[2,2,3],[3,3,3]])

