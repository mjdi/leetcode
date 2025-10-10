import leetcode75.dshelper.treenode as tn
from leetcode75._1448.solution import Solution as sol

class TestClass:
    def test_one(self):
        root = tn.create_binary_tree([3,1,4,3,None,1,5])
        assert 4 == sol.goodNodes(root)

    def test_two(self):
        root = tn.create_binary_tree([3,3,None,4,2])
        assert 3 == sol.goodNodes(root)

    def test_three(self):
        root = tn.create_binary_tree([1])
        assert 1 == sol.goodNodes(root)