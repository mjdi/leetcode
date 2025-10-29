from leetcode75._338.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [0,1,1] == sol().countBits(2)

    def test_two(self):
        assert [0,1,1,2,1,2] == sol().countBits(5)

    def test_three(self):
        assert [0,1,1,2,1,2,2,3] == sol().countBits(7)

