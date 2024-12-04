from typing import List

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def next_char(char):
            if char == "z":
                return "a"
            else:
                return chr(ord(char) + 1)

        i = 0 # pointer for str1
        for j in range(len(str2)):
            while i < len(str1) and str1[i] != str2[j] and next_char(str1[i]) != str2[j]:
                i += 1 #f fast forward
            if i == len(str1):
                return False
            
            i += 1 # find next potential char

        return True