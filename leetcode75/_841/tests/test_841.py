from leetcode75._841.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert True == sol().canVisitAllRooms([[1],[2],[3],[]])

    def test_two(self):
        assert False == sol().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])

    def test_three(self):
        assert True == sol().canVisitAllRooms([[1],[3],[0],[2]])

