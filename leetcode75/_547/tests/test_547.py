from leetcode75._547.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 2 == sol().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])

    def test_two(self):
        assert 3 == sol().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])

    def test_three(self):
        assert 2 == sol().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]])

