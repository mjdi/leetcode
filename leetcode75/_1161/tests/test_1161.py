import leetcode75.dshelper.treenode as tn
from leetcode75._1161.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        ask = tn.create_binary_tree([1,7,0,7,-8,None,None])
        assert 2 == sol().maxLevelSum(ask)

    def test_two(self):
        ask = tn.create_binary_tree([989,None,10250,98693,-89388,None,None,None,-32127])
        assert 2 == sol().maxLevelSum(ask)

    def test_three(self):
        ask = tn.create_binary_tree([100,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        assert 1 == sol().maxLevelSum(ask)

