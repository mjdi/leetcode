from leetcode75._2390.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert "lecoe" == sol().removeStars("leet**cod*e")

    def test_two(self):
        assert "" == sol().removeStars("erase*****")

    def test_three(self):
        assert "hw" == sol().removeStars("he*l*l*o*wo*r*l*d*")

