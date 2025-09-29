from leetcode75._2095.solution import Solution as sol
import leetcode75.dshelper.linked_list as dsh
                
class TestClass:
    def test_one(self):
        ask = dsh.create_linked_list([1,3,4,7,1,2,6])
        ans = dsh.create_linked_list([1,3,4,1,2,6])
        assert dsh.compare_linked_lists(ans,sol.deleteMiddle(ask))

    def test_two(self):
        ask = dsh.create_linked_list([1,2,3,4])
        ans = dsh.create_linked_list([1,2,4])
        assert dsh.compare_linked_lists(ans,sol.deleteMiddle(ask))

    def test_three(self):
        ask = dsh.create_linked_list([2,1])
        ans = dsh.create_linked_list([2])
        assert dsh.compare_linked_lists(ans,sol.deleteMiddle(ask))

