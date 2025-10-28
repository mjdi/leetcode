# https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=leetcode-75
import copy   
class Trie:

    def __init__(self):
        self.hm = {}        

    def insert(self, word: str) -> None:
        d = self.hm
        for i, let in enumerate(word):
            if let not in d:
                d[let] = {}
            if i == len(word) - 1:
                d[let]['eow'] = {} # end of word marker
            d = d[let]

    def search(self, word: str) -> bool:
        # d = copy.deepcopy(self.hm)
        d = self.hm
        for i, let in enumerate(word):
            if let in d:
                if i == len(word) - 1 and 'eow' in d[let]:
                    return True
                d = d[let]
            else:
                return False
        return False 

    def startsWith(self, prefix: str) -> bool:
        d = self.hm
        for let in prefix:
            if let in d:
                d = d[let]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


