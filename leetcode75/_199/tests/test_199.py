import leetcode75.dshelper.treenode as tn
from leetcode75._199.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        ask = tn.create_binary_tree([1,2,3,None,5,None,4])
        assert [1,3,4] == sol().rightSideView(ask)

    def test_two(self):
        ask = tn.create_binary_tree([1,2,3,4,None,None,None,5])
        assert [1,3,4,5] == sol().rightSideView(ask)

    def test_three(self):
        ask = tn.create_binary_tree([1,None,3])
        assert [1,3] == sol().rightSideView(ask)

    def test_four(self):
        ask = tn.create_binary_tree([])
        assert [] == sol().rightSideView(ask)