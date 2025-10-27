# https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=leetcode-75
from collections import deque
from typing import Optional, List
                
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
# code that I found afterwards that is more succint/pythonic but essentially the same 
# https://leetcode.com/problems/evaluate-division/solutions/88275/python-fast-bfs-solution-with-detailed-explantion/?envType=study-plan-v2&envId=leetcode-75

        graph = {}
        
        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
            
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value)
        
        def find_path(query):
            b, e = query
            
            if b not in graph or e not in graph:
                return -1.0
                
            q = deque([(b, 1.0)])
            visited = set()
            
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
            
            return -1.0
        
        build_graph(equations, values)
        return [find_path(q) for q in queries]

# my code that I submitted, (not as clean but same concepts)

        # self.numers = {} # numerators, foward ref to denominators of equations
        # for eq, value in zip(equations, values):
        #     numer, denom = eq[0], eq[1]
        #     if numer not in self.numers: # 
        #         self.numers[numer] = {'denoms':[], 'values':[]}
        #     self.numers[numer]['denoms'].append(denom)
        #     self.numers[numer]['values'].append(value)
        #     if denom not in self.numers: # store inverse as well 
        #         self.numers[denom] = {'denoms':[], 'values':[]}
        #     self.numers[denom]['denoms'].append(numer)
        #     self.numers[denom]['values'].append(1/value)
        
        # def dfs(ans, numer, visited, end_denom):
        #     if numer not in self.numers:
        #         return ans, False 
        #     if numer in visited:
        #         return ans, False
        #     visited.append(numer)
        #     denoms = self.numers[numer]["denoms"]
        #     values = self.numers[numer]["values"]
        #     old_ans = ans
        #     for denom, value in zip(denoms, values):
        #         new_ans = old_ans * value 
        #         if denom == end_denom: # if found goal denominator
        #             return new_ans, True
        #         ans, success = dfs(new_ans, denom, visited, end_denom)
        #         if success:
        #             return ans, True
        #     return ans, False 

        # self.ans = []
        # for q in queries:
        #     numer, denom = q[0], q[1]
        #     if numer in self.numers and denom in self.numers:
        #         success = False
        #         if numer == denom:
        #             self.ans.append(1)
        #             continue
        #         if numer in self.numers:
        #             ans,success = (dfs(1, numer, visited = [], end_denom=denom))
        #         if success:
        #             self.ans.append(ans)
        #         else:
        #             self.ans.append(-1)
        #     else:
        #         self.ans.append(-1)
                
        # return self.ans
