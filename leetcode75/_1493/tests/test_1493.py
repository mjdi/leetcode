from leetcode75._1493.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert 3 == sol.longestSubarray([1,1,0,1])

    def test_two(self):
        assert 5 == sol.longestSubarray([0,1,1,1,0,1,1,0,1])  

    def test_three(self):
        assert 2 == sol.longestSubarray([1,1,1])

