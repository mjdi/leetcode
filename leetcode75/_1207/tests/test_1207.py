from leetcode75._1207.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert True == sol.uniqueOccurrences([1,2,2,1,1,3])

    def test_two(self):
        assert False == sol.uniqueOccurrences([1,2])

    def test_three(self):
        assert True == sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])

