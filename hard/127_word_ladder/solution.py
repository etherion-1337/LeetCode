from typing import List
from collections import deque, defaultdict

class Solution:
    """
    graph + BFS
    each node is a word, each edge is a transformation (single edit distance)
    find the shortest path from beginWord to endWord
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # create adjacency list: {pattern: [word]}
        # e.g. {*it : [hit, hot]}
        # use a wild card pattern such that this process is n*m^2
        # if use double loop is is n^2*m which will TLE
        neighbor_map = defaultdict(list)
        wordList.append(beginWord) # wordList does not contain begin word
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbor_map[pattern].append(word) 
        # BFS
        visited = set([beginWord])
        q = deque([beginWord])
        result = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in neighbor_map[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            result += 1

        return 0
    
class NeetSolution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
