from leetcode75._328.solution import Solution as sol
import leetcode75.dshelper.linked_list as dsh
                
class TestClass:
    def test_one(self):
        ask = dsh.create_linked_list([1,2,3,4,5])
        ans = dsh.create_linked_list([1,3,5,2,4])
        assert dsh.compare_linked_lists(ans,sol.oddEvenList(ask))

    def test_two(self):
        ask = dsh.create_linked_list([2,1,3,5,6,4,7])
        ans = dsh.create_linked_list([2,3,6,7,1,5,4])
        assert dsh.compare_linked_lists(ans,sol.oddEvenList(ask))

    def test_three(self):
        ask = dsh.create_linked_list([1,4,2,5,3,6])
        ans = dsh.create_linked_list([1,2,3,4,5,6])
        assert dsh.compare_linked_lists(ans,sol.oddEvenList(ask))