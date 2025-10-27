from leetcode75._374.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 6== sol().guessNumber(10,6)

    def test_two(self):
        assert 1 == sol().guessNumber(1,1)

    def test_three(self):
        assert 1 == sol().guessNumber(2,1)

    def test_four(self):
        assert 2 == sol().guessNumber(2,2)

    def test_five(self):
        assert 4 == sol().guessNumber(5,4)