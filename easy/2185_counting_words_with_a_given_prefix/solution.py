from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for w in words:
            if w.startswith(pref):
                ans += 1

        return ans
    

class TrieNode():
    """
    Trie solution
    """
    def __init__(self):
        self.children = {} # a -> TrieNode
        self.count = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        curr = self.root
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1

    def count(self, pref):
        curr = self.root
        for c in pref:
            if c not in curr.children:
                return 0
            curr = curr.children[c]

        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_tree = Trie()

        for w in words:
            if len(w) >= len(pref):
                prefix_tree.add(w)
