import leetcode75.dshelper.treenode as tn
from leetcode75._104.solution import Solution as sol

class TestClass:
    def test_one(self):
        ask = tn.create_binary_tree([3,9,20,1,None,None,15])
        assert 3 == sol().maxDepth(ask)
    def test_two(self):
        ask = tn.create_binary_tree([1,None,2])
        assert 2 == sol().maxDepth(ask)

 