from typing import Optional

class Node:
    """
    Definition for a Node.
    """
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    DFS solution
    time complexity: O(v+e)
    """
    def dfs(self, node):
        if node in self.old2new:
            return self.old2new[node]

        clone = Node(node.val)
        self.old2new[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor))
        return clone

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.old2new = {}
        if node:
            new_node = self.dfs(node)
        else:
            new_node = None

        return new_node


class NeetSolution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

    
