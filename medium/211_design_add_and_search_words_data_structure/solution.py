class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def dfs(self, j, root, word):
        curr = root

        for i in range(j, len(word)):
            char = word[i]
            if char == ".":
                for child in curr.children.values():
                    if self.dfs(i+1, child, word): # i + 1 because we are skipping "."
                        return True
                return False
            else:
                if char not in curr.children:
                    return False
                curr = curr.children[char]
        return curr.end_of_word # e.g. if a full word is found, then only else is executed and return True
        
    def search(self, word: str) -> bool:
        search_result = self.dfs(0, self.root, word)

        return search_result
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class NeetWordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
