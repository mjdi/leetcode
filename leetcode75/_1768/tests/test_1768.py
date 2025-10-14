from leetcode75._1768.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        
        assert "apbqcr" == sol().mergeAlternately("abc","pqr")

    def test_two(self):
        assert "apbqrs" == sol().mergeAlternately("ab", "pqrs")

    def test_three(self):
        assert "apbqcd" == sol().mergeAlternately("abcd","pq")

