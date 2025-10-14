from leetcode75._443.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        # ["a","2","b","2","c","3"]
        assert 6 == sol().compress(["a","a","b","b","c","c","c"])

    def test_two(self):
        # ["a"]
        assert 1 == sol().compress(["a"])

    def test_three(self):
        # ["a","b","1","2"]
        assert 4 == sol().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

