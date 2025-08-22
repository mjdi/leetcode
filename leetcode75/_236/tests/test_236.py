import leetcode75.dshelper.treenode as tn
from leetcode75._236.solution import Solution as sol

class TestClass:
    def test_one(self):
        root = tn.create_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
        assert 3 == sol.lowestCommonAncestor(root, p=5, q=1)
        
    def test_two(self):
        root = tn.create_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
        assert 5 == sol.lowestCommonAncestor(root, p=5, q=4)
    
    def test_three(self):
        root = tn.create_binary_tree([1,2])
        assert 1 == sol.lowestCommonAncestor(root, p=1, q=2)

    