import leetcode75.dshelper.linked_list as dsh
# from leetcode75._206.solution import Solution as sol
from leetcode75._206.solution_recursive import Solution as sol
import pytest

@pytest.fixture(scope="class")
def setup_my_feature():
    print("\nSetting up MyFeature for the class...")
    yield
    print("\nTearing down MyFeature for the class...")

# Test Cases:
# 1. [1,2,3,4,5]
# 2. [1,2,3]
# 3. [1,2]
# 4. [1]
# 5. []

class TestClass:
    def test_one(self):
        ask = dsh.create_linked_list([1,2,3,4,5])
        ans = dsh.create_linked_list([5,4,3,2,1])
        assert dsh.compare_linked_lists(ans, sol.reverseList(ask))

    def test_two(self):
        ask = dsh.create_linked_list([1,2,3])
        ans = dsh.create_linked_list([3,2,1])
        assert dsh.compare_linked_lists(ans, sol.reverseList(ask))
        
    def test_three(self):
        ask = dsh.create_linked_list([1,2])
        ans = dsh.create_linked_list([2,1])
        assert dsh.compare_linked_lists(ans, sol.reverseList(ask))
        
    def test_four(self):
        ask = dsh.create_linked_list([1])
        ans = dsh.create_linked_list([1])
        assert dsh.compare_linked_lists(ans, sol.reverseList(ask))

    def test_empty(self):
        ask = dsh.create_linked_list([])
        ans = dsh.create_linked_list([])
        assert dsh.compare_linked_lists(ans, sol.reverseList(ask))
