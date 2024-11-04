class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        count = 1
        char = word[0]

        for i in range(1, len(word)):
            if word[i] != word[i-1] or count == 9:
                ans += str(count) + char
                count = 1
                char = word[i]
            else:
                count += 1

        # take care of trailing char that not yet counted
        ans += str(count) + char

        return ans