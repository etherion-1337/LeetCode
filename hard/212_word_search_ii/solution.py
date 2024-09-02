from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self # refer to the root node
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    """
    Use Trie to store the words, and then do DFS on the Trie and the board
    """
    def dfs(self, r, c, node, word):
        if (r < 0 or c < 0 or
            r == self.ROWS or c == self.COLS or
            (r, c) in self.visit or self.board[r][c] not in node.children):
            return

        self.visit.add((r, c))
        node = node.children[self.board[r][c]]
        word += self.board[r][c]
        if node.isWord:
            self.result.add(word)

        self.dfs(r + 1, c, node, word)
        self.dfs(r - 1, c, node, word)
        self.dfs(r, c + 1, node, word)
        self.dfs(r, c - 1, node, word)
        self.visit.remove((r, c))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        self.board = board
        for w in words:
            root.addWord(w)

        self.ROWS, self.COLS = len(board), len(board[0])
        self.result, self.visit = set(), set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.dfs(r, c, root, "")

        return list(self.result)
    

class NeetSolution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        result, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(result)