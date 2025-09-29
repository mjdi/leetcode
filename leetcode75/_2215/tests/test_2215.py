from leetcode75._2215.solution import Solution as sol

class TestClass:
    def test_one(self):
        assert [[1,3],[4,6]] == sol.findDifference([1,2,3], [2,4,6])

    def test_two(self):
        assert [[3],[]] == sol.findDifference([1,2,3,3], [1,1,2,2])   

    def test_three(self):
        assert [[1,3,5],[]] == sol.findDifference([1,2,3,4,5], [2,4])

