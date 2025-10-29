from leetcode75._994.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 4 == sol().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])

    def test_two(self):
        assert -1 == sol().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])

    def test_three(self):
        assert 0 == sol().orangesRotting([[0,2]])

