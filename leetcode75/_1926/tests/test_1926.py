from leetcode75._1926.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 1 == sol().nearestExit(
            [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
            [1,2]
        )

    def test_two(self):
        assert 2 == sol().nearestExit(
            [["+","+","+"],[".",".","."],["+","+","+"]],
            [1,0]
        )

    def test_three(self):
        assert -1 == sol().nearestExit(
            [[".","+"]],
            [0,0]
        )

