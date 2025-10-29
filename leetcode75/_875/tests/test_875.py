from leetcode75._875.solution import Solution as sol

class TestClass:
    def test_one(self):
        assert 4 == sol().minEatingSpeed([3,6,7,11], 8)

    def test_two(self):
        assert 30 == sol().minEatingSpeed([30,11,23,4,20], 5)

    def test_three(self):
        assert 23 == sol().minEatingSpeed([30,11,23,4,20], 6)
