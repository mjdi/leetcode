from leetcode75._739.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [1,1,4,2,1,1,0,0] == sol().dailyTemperatures([73,74,75,71,69,72,76,73])

    def test_two(self):
        assert [1,1,1,0] == sol().dailyTemperatures([30,40,50,60])

    def test_three(self):
        assert [1,1,0] == sol().dailyTemperatures([30,60,90])
    
