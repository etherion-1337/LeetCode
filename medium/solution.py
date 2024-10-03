class Solution:
    """
    2D DP bottom-up approach

    time complexity: O(m*n), where m is the length of text1 and n is the length of text2
    space complexity: O(m*n), where m is the length of text1 and n is the length of text2

    we need a dp array of size (len(text1)+1) x (len(text2)+1), 
    the extra row and column at the most right and bottom are filled with 0, and serve as the out-of-boundary condition.
    at each cell, we cache the length of the longest common subsequence of the two substrings that start from the current cell (i, j) to the end of the two strings.

    1. when text1[i] == text2[j], we know that the current character is part of the common subsequence, so we increment the length of the common subsequence by 1, on top of the cell diagonally (i+1, j+1).
    2. when text1[i] != text2[j], we know that the current character is not part of the common subsequence, so we take the maximum of the two possible subsequences that we can get by skipping either the current character in text1 or text2.
    -> this means the cell to the right and the cell below the current cell.
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # extra row and column at the most right and bottom are filled with 0
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        # start from bottom right
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]