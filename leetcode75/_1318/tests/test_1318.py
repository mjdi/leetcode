from leetcode75._1318.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 3 == sol().minFlips(2,6,5)

    def test_two(self):
        assert 1 == sol().minFlips(4,2,7)

    def test_three(self):
        assert 0 == sol().minFlips(1,2,3)

    def test_four(self):
        assert 3 == sol().minFlips(8,3,5)