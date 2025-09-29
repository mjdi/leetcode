from leetcode75._283.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [1,3,12,0,0] == sol.moveZeroes([0,1,0,3,12])

    def test_two(self):
        assert [0] == sol.moveZeroes([0])

    def test_three(self):
        assert [1,2,3,0,0,0] == sol.moveZeroes([0,0,0,1,2,3])

