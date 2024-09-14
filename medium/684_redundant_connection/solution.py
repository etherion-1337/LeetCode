from typing import List

class Solution:
    """
    Union find
    very similar to question 323
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # array to track each node's parents
        parents = [i for i in range(len(edges) + 1)]
        # array to track the rank or size of the cluster the node belongs to
        rank = [1]*(len(edges) + 1)

        def find(n):
            """
            Given a node, find its (root parents)
            """
            p = parents[n]
            # if equal, we have reached the top, since each node is its own parents
            while p != parents[p]:
                # path compression, make linked list shorter
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # same root -> no union
            if p1 == p2:
                return False
            # check rank, add smaller rank to bigger rank cluster
            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return True

        for n1, n2 in edges:
            _tmp = union(n1, n2)
            if not _tmp:
                return [n1, n2]
            
class NeetSolution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
