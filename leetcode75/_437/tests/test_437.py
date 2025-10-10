import leetcode75.dshelper.treenode as tn
from leetcode75._437.solution import Solution as sol

class TestClass:
    def test_one(self):
        root = tn.create_binary_tree([10,5,-3,3,2,None,11,3,-2,None,1])
        assert 3 == sol().pathSum(root, targetSum=8)
        
    def test_two(self):
        root = tn.create_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
        assert 3 == sol().pathSum(root, targetSum=22)

    def test_three(self):
        root = tn.create_binary_tree([1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1])
        assert 22 == sol().pathSum(root, targetSum=0)

    def test_four(self):
        root = tn.create_binary_tree([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        assert 49 == sol().pathSum(root, targetSum=0)

    def test_five(self):
        root = tn.create_binary_tree([1,-2,3,-4,5,-6,7,-8,9,-10,11,-12,13,-14,15])
        assert 2 == sol().pathSum(root, targetSum=7)

    def test_six(self):
        root = tn.create_binary_tree([0,0,0])
        assert 5 == sol().pathSum(root, targetSum=0)

    def test_seven(self):
        root = tn.create_binary_tree([0,0,0,0,0,0,0])
        assert 17 == sol().pathSum(root, targetSum=0)