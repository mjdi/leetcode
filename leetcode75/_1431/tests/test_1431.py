from leetcode75._1431.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [True,True,True,False,True] == sol().kidsWithCandies([2,3,5,1,3], 3)

    def test_two(self):
        assert [True,False,False,False,False] == sol().kidsWithCandies([4,2,1,1,2] ,1)

    def test_three(self):
        assert [True,False,True] == sol().kidsWithCandies([12,1,12], 10)

