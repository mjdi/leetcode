from leetcode75._2300.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [4,0,3] == sol().successfulPairs(
            [5,1,3],
            [1,2,3,4,5],
            7)

    def test_two(self):
        assert [2,0,2] == sol().successfulPairs(
            [3,1,2],
            [8,5,8],
            16)

    def test_three(self):
        assert [3,0,0] == sol().successfulPairs(
            [4,3,2],
            [1,1,1,2,2,2,3,3,3,4,4,4],
            16)

    def test_four(self):
        assert [1,0,1] == sol().successfulPairs(
            [5,1,4],
            [2],
            7
        )