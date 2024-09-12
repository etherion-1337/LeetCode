from typing import List

class Solution:
    def dfs(self, node, prev):
        if node in self.visited:
            return False

        self.visited.add(node)
        for adj in self.adj_map[node]:
            # edge case is when we do dfs, if we visit prev node, we should skip it
            if adj == prev:
                continue
            if not self.dfs(adj, node):
                return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        self.adj_map = {i:[] for i in range(n)}
        # since it is undirected we add them into both
        for n1, n2 in edges:
            self.adj_map[n1].append(n2)
            self.adj_map[n2].append(n1)

        self.visited = set()
        # check we have visited exactly all nodes -> check if graph is connected
        # check no cycle
        return self.dfs(0,-1) and n == len(self.visited)

class NeetSolution:
    """
    check 2 things:
    1) if the graph is connected: i.e. visited all nodes
    2) if there is no cycle: i.e. no node is visited twice
    edge case is when we do dfs, if we visit prev node, we should skip it
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i: int, prev: int) -> bool:
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)