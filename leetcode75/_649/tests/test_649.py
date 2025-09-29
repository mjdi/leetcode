from leetcode75._649.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert "Radiant" == sol.predictPartyVictory('RD')

    def test_two(self):
        assert "Dire" == sol.predictPartyVictory('RDD')

    def test_three(self):
        assert "Dire" == sol.predictPartyVictory("RDDRDRDRRDDR")

