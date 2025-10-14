from leetcode75._735.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [5,10] == sol().asteroidCollision([5,10,-5])

    def test_two(self):
        assert [] == sol().asteroidCollision([8,-8])

    def test_three(self):
        assert [10] == sol().asteroidCollision([10,2,-5])

