from leetcode75._2336.solution import SmallestInfiniteSet
                
class TestClass:
    def test_one(self):
        obj = SmallestInfiniteSet()
        obj.addBack(2)
        obj.popSmallest()
        obj.popSmallest()
        obj.popSmallest()
        obj.addBack(1)
        obj.popSmallest()
        assert 4 == obj.popSmallest()

