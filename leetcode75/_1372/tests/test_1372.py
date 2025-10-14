import leetcode75.dshelper.treenode as tn
from leetcode75._1372.solution import Solution as sol

class TestClass:
    def test_one(self):
        root = tn.create_binary_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
        assert 3 == sol().longestZigZag(root)
        
    def test_two(self):
        root = tn.create_binary_tree([1,1,1,None,1,None,None,1,1,None,1])
        assert 4 == sol().longestZigZag(root)
        
    def test_three(self):
        root = tn.create_binary_tree([1])
        assert 0 == sol().longestZigZag(root)
    