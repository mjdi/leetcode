from leetcode75._1466.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 3 == sol().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])

    def test_two(self):
        assert 2 == sol().minReorder(5, [[1,0],[1,2],[3,2],[3,4]])

    def test_three(self):
        assert 0 == sol().minReorder(3, [[1,0],[2,0]])
    
    def test_four(self):
        assert 3 == sol().minReorder(6, [[1,3],[2,3],[4,0],[4,5],[0,1]])

