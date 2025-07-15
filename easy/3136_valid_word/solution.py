class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if len(word) >= 3 and word.isalnum():
            vow = 0
            con = 0
            for c in word:
                if c.lower() in vowels:
                    vow += 1
                elif c.isalpha():
                    con += 1
            if vow > 0 and con > 0:
                return True

        return False