from leetcode75._208.solution import Trie
                
class TestClass:
    def test_one(self):
        trie = Trie()
        trie.insert("apple")
        assert True  == trie.search("apple")   
        assert False == trie.search("app")
        assert True  == trie.startsWith("app")
        trie.insert("app");
        assert True  == trie.search("app")  
