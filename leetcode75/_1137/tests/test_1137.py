from leetcode75._1137.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 4 == sol().tribonacci(4)

    def test_two(self):
        assert 1389537 == sol().tribonacci(25)

    def test_three(self):
        assert 2082876103 == sol().tribonacci(37)

