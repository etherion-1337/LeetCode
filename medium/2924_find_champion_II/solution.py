from typing import List

class Solution:
    """
    time complexity: O(n+v) where n is the number of nodes and v is the number of edges
    """
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # adjacency list
        # key: node, value: list of nodes that point TOWARDS the key
        # it is like a reversed adjacency list
        adj_list = {i:[] for i in range(n)}
        for src, dst in edges:
            adj_list[dst].append(src)

        ans = []
        # if more than 1 node has no incoming edges, return -1
        for k,v in adj_list.items():
            if not v:
                ans.append(k)
        
        return ans[0] if len(ans) == 1 else -1
    

class NeetSolution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src, dst in edges:
            incoming[dst] += 1

        champions = []
        for i, incoming_cnt in enumerate(incoming):
            if not incoming_cnt:
                champions.append(i)

        if len(champions) > 1:
            return -1

        return champions[0]