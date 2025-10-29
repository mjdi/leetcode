import leetcode75.dshelper.treenode as tn
from leetcode75._450.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        ask = tn.create_binary_tree([5,3,6,2,4,None,7])
        ans = tn.create_binary_tree([5,4,6,2,None,None,7])
        assert tn.write_binary_tree_as_list(ans) == \
               tn.write_binary_tree_as_list(sol().deleteNode(ask, 3))  

    def test_two(self):
        ask = tn.create_binary_tree([5,3,6,2,4,None,7])
        assert ask == sol().deleteNode(ask, 0)

    def test_three(self):
        ask = tn.create_binary_tree([])
        assert [] == tn.write_binary_tree_as_list(sol().deleteNode(ask, 0))

    def test_four(self):
        ask = tn.create_binary_tree([1])
        assert [1] == tn.write_binary_tree_as_list(sol().deleteNode(ask, 0))
        
    def test_five(self):
        ask = tn.create_binary_tree([5,3,6,2,4,None,7])
        ans = tn.create_binary_tree([6,3,7,2,4])
        assert tn.write_binary_tree_as_list(ans) == \
               tn.write_binary_tree_as_list(sol().deleteNode(ask, 5))

    def test_six(self):
        ask = tn.create_binary_tree([1,None,2])
        ans = tn.create_binary_tree([2])
        assert tn.write_binary_tree_as_list(ans) == \
               tn.write_binary_tree_as_list(sol().deleteNode(ask, 1))