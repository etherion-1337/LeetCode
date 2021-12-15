class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {char for char in "aeiou"}
        ans = "".join([char for char in s if char not in vowels])
        return ans

if __name__ == "__main__":
    soln = Solution()
    _input = "leetcodeisacommunityforcoders"
    answer = soln.removeVowels(_input)
    print(answer)