from typing import List

class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        curr = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in curr.children:
                curr.children[(c1, c2)] = TrieNode()
            curr = curr.children[(c1, c2)]
            curr.count += 1

    def count(self, w):
        curr = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in curr.children:
                return 0
            curr = curr.children[(c1, c2)]
        return curr.count

class Solution:
    """
    Trie solution

    Each node we keep track both prefix and suffix. We can use a tuple (c1, c2) to represent the edge between two nodes.
    """
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        root = Trie()

        for w in reversed(words):
            ans += root.count(w) # count before add, because every word is suffix and prefix of itself
            root.add(w)

        return ans