from typing import List

# TODO: DFS solution

class Solution:
    """
    Union find solution
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # array to track each nodes parents
        parents = [i for i in range(n)]
        # array to track the rank or size of the cluster the node belongs to
        rank = [1]*n

        def find(n1):
            """
            given a node, find its (root) parent
            """
            res = n1
            # if equal, we have reached the top, since each node is its own parents
            while res != parents[res]:
                # path compression, make linked list shorter
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # same root -> no union
            if p1 == p2:
                return 0
            # check rank, add smaller rank to bigger rank cluster
            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
        return result
    
class UnionFind:

    def __init__(self):
        self.f = {}

    def findParent(self, x: int) -> int:
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x: int, y: int):

        self.f[self.findParent(x)] = self.findParent(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))
    