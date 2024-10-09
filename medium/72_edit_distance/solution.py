class NeetSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        2D bottom up DP

        we will cache a 2D grid of (len(w1)+1)*(len(w2)+1)
        i: index in w1, j: index in w2 which isht target
        at each cell dp[i][j], we cache the minimum edit distance for w1[i:] to approach w2[j:]
        the extra row and col is for emptry string and base cases.

        if w1[i] == w2[j]: we look at [i+1][j+1] and edit distance unchagned
        else: (need +1 edit operation/distance)
            insert: [i][j+1] since we insert a char in w1 so we can move to the next char in w2
            delete: [i+1][j] since we move del a char from i we move to the next, but j in w2 is still not matched so it remains
            replace: [i+1][j+1] since we matched a char from both w1 and w2 we move to the next char in both

            a  c  d  
        a           3
        b    1      2
        d       0   1
          3  2  1   0
        from bottom right, if both w1[1] == w2[2] match, we use diag element
        else, we choose the minimun from right, diag and below, and plus 1

        time complexity: O(m*n)
        space complexity: O(m*n)
        """
        # populate the board
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        # populate most right and bottom 
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        # from bottom right do bottom up DP
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]