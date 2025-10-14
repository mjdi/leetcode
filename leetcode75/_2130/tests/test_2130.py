import leetcode75.dshelper.linked_list as dsh
from leetcode75._2130.solution import Solution as sol

class TestClass:
    def test_one(self):
        ask = dsh.create_linked_list([5,4,2,1])
        assert 6 == sol().pairsum(ask)

    def test_two(self):
        ask = dsh.create_linked_list([4,2,2,3])
        assert 7 == sol().pairsum(ask)
        
    def test_three(self):
        ask = dsh.create_linked_list([1,10000])
        assert 10001 == sol().pairsum(ask)
        
    def test_four(self):
        ask = dsh.create_linked_list([9,5,4,2,2,3,2,8,3,1])
        assert 12 == sol().pairsum(ask)
        
