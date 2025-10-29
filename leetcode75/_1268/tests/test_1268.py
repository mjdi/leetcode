from leetcode75._1268.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]] == \
        sol().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], 'mouse')

    def test_two(self):
        assert [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]] == \
        sol().suggestedProducts(['havana'], 'havana')

    # def test_three(self):
    #     assert == sol().

