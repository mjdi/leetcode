from leetcode75._901.solution import StockSpanner
                
class TestClass:
    def test_one(self):
        stockSpanner = StockSpanner();
        assert 1 == stockSpanner.next(100); 
        assert 1 == stockSpanner.next(80);  
        assert 1 == stockSpanner.next(60);  
        assert 2 == stockSpanner.next(70);  
        assert 1 == stockSpanner.next(60);  
        # because the last 4 prices (including today's price of 75)
        # were less than or equal to today's price.
        assert 4 == stockSpanner.next(75); 
        assert 6 == stockSpanner.next(85);  

