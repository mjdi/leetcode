# https://leetcode.com/problems/search-suggestions-system/?envType=study-plan-v2&envId=leetcode-75
from typing import List
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
    
    def _backtrack(self, trie_node):
        if 'eow' in trie_node:
            self.res.append(self.sol) 
    
        for k in trie_node.keys():
            if k == 'eow':
                continue
            self.sol = self.sol + k
            self._backtrack(trie_node[k])
            self.sol = self.sol[:-1]

    def return_completions(self, prefix:str) -> List[str]:
        if not self.startsWith(prefix):
           return [] 
        
        d = self.hm
        for let in prefix:
            if let in d:
                d = d[let]

        self.res = []
        self.sol = prefix

        self._backtrack(d)

        return self.res             
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        for p in products:
            t.insert(p)
        autocompletions = []
        for i in range(len(searchWord)):
            prefix = searchWord[0:i+1]
            all_autocompletions = t.return_completions(prefix)
            autocompletions.append(sorted(all_autocompletions)[0:3]) 
        return autocompletions

