from typing import List

class Solution:
    """
    DFS + backtracking
    TLE
    time complexity: O(V+e)^2
    """
    def dfs(self, src):
        # went through all edges
        if len(self.result) == len(self.tickets) + 1:
            return True
        # we have meet a deadend
        # but havent finish all tickets
        if src not in self.adj:
            return False
        # clone the adj list for that src
        temp = list(self.adj[src])
        for i, v in enumerate(temp):
            self.adj[src].pop(i)
            self.result.append(v)
            if self.dfs(v): return True
            # if fail, backtrack
            self.adj[src].insert(i,v)
            self.result.pop()
        return False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = {src: [] for src, dst in tickets}
        # this sort src then dst
        self.tickets = tickets
        self.tickets.sort()
        # populate adjacency list
        for src, dst in self.tickets:
            self.adj[src].append(dst)
        self.result = ["JFK"]
        
        self.dfs("JFK")
        return self.result
    
class Solution:
    def dfs(self, src):
        if src in self.adj:
            # clone all the destination from that src
            destinations = self.adj[src][:]
            while destinations:
                dest = destinations[0]
                self.adj[src].pop(0)
                self.dfs(dest)
                destinations = self.adj[src][:]

        self.result.append(src)
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adjacency list {source : [destination]}
        self.adj = {src: [] for src, dst in tickets}
        self.result = []
        # populate adjaency list
        for src, dst in tickets:
            self.adj[src].append(dst)
        # sort destinations -> we need to search by lexical order
        for key in self.adj:
            self.adj[key].sort()
        
        self.dfs("JFK")
        self.result.reverse()

        if len(self.result) != len(tickets) + 1:
            return []
        return self.result