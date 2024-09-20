from typing import List

class Solution:
    def dfs(self, c):
        if c in self.visited:
            # if visited, return visited status, e.g. True if current path saw b4 and therefore detected a cyclic path
            return self.visited[c]
        # now it is in current path
        self.visited[c] = True
        for neigh in self.adj[c]:
            if self.dfs(neigh):
                return True
        # released -> no long in current path
        self.visited[c] = False
        # post order dfs -> add this node when finish all its neigh
        self.result.append(c)


    def alienOrder(self, words: List[str]) -> str:
        """
        post order DFS
        """
        # build adjacency list
        # key: char
        # val: set of char that is lexicographically behind the key according to words given
        adj = {c:set() for w in words for c in w}
        for i in range(len(words) - 1): # for every pairs
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # edge case for if 2 words has the same prefix, but the longer word is sorted in front
            # then this is invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            # populate the adj list
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    # only find the first char diff for each pair since it is only useful for that info
                    # anything after that the order of char doesnt provide any info due to definition of lexico sort
                    break
        # False: visited, True: visited and it is in current path -> lead to cyclic
        self.visited = {}
        self.result = []
        self.adj = adj

        for c in adj:
            if self.dfs(c):
                return ""
        self.result.reverse()
        return "".join(self.result)