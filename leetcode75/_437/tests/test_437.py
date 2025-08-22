import leetcode75.dshelper.treenode as tn
from leetcode75._437.solution import Solution as sol

class TestClass:
    def test_one(self):
        root = tn.create_binary_tree([10,5,-3,3,2,None,11,3,-2,None,1])
        assert 3 == sol.pathSum(root, targetSum=8)
        
    def test_two(self):
        root = tn.create_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
        assert 3 == sol.pathSum(root, targetSum=22)

    