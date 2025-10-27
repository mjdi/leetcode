from leetcode75._399.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [6.00000,0.50000,-1.00000,1.00000,-1.00000] == \
            sol().calcEquation(
                [["a","b"],["b","c"]],
                [2.0,3.0],
                [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
            )

    def test_two(self):
        assert [3.75000,0.40000,5.00000,0.20000] == \
            sol().calcEquation(
                [["a","b"],["b","c"],["bc","cd"]],
                [1.5,2.5,5.0],
                [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
            )

    def test_three(self):
        assert [0.50000,2.00000,-1.00000,-1.00000] == \
            sol().calcEquation(
                [["a","b"]],
                [0.5],
                [["a","b"],["b","a"],["a","c"],["x","y"]]
            )
    
    def test_four(self):
        assert [4/3,1.00000,-1.00000] == \
            sol().calcEquation(
                [["a","e"],["b","e"]],
                [4.0,3.0],
                [["a","b"],["e","e"],["x","x"]]
            )
            
    def test_five(self):
        assert [120,1/5/4/3/2] == \
            sol().calcEquation(
                [["a","b"],["b","c"],["c","d"],["d","e"]],
                [2.0,3.0,4.0,5.0],
                [["a","e"], ["e","a"]]
            )
