import leetcode75.dshelper.treenode as tn
from leetcode75._700.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        ask = tn.create_binary_tree([4,2,7,1,3])
        assert ask.left == sol().searchBST(ask, 2)

    def test_two(self):
        ask = tn.create_binary_tree([4,2,7,1,3])
        assert None == sol().searchBST(ask, 5)

    def test_three(self):
        ask = tn.create_binary_tree([4])
        assert ask == sol().searchBST(ask, 4)

