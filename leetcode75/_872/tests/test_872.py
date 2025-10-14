import leetcode75.dshelper.treenode as tn
from leetcode75._872.solution import Solution as sol

class TestClass:
    def test_one(self):
        tree1 = tn.create_binary_tree([3,5,1,6,2,9,8,None,None,7,4])
        tree2 = tn.create_binary_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        assert True == sol().leafSimilar(tree1,tree2)
    def test_two(self):
        tree1 = tn.create_binary_tree([1,2,3])
        tree2 = tn.create_binary_tree([1,3,2])
        assert False == sol().leafSimilar(tree1,tree2)