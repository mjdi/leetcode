from leetcode75._933.solution import RecentCounter
                
class TestClass:
    def test_one(self):
        rc = RecentCounter()
        pings = [None]
        pings.append(rc.ping(1))
        pings.append(rc.ping(100))
        pings.append(rc.ping(3001))
        pings.append(rc.ping(3002))
        assert [None,1,2,3,3] == pings
