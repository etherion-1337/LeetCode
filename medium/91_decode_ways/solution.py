class Solution:
    def dfs(self, i, s):
        """
        i means string start from i -> eos, to find how many ways of decode can be found for this substring
        """
        # if this index already solved -> obtained num of ways of decode
        # or we reached (beyond) end of str
        if i in self.dp:
            return self.dp[i]
        # if char is 0, then it is not possible to decode
        if s[i] == "0":
            return 0

        # go for next char
        result = self.dfs(i + 1, s)
        # if i + 1 never out of bound and curr one is either 1 or 2 (2 must also satsify the next char is in 0-6)
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            # num of ways from the previous one is being added tgt
            result += self.dfs(i + 2, s)
        # update the cache, this is the dp part
        self.dp[i] = result
        return result

    def numDecodings(self, s: str) -> int:
        """
        dp (recursive) approach

        time complexity O(n)
        space complexity O(n)

        note the way dfs works is to process the str backwards (i.e. s[-1] first)
        """
        # dp cache to store num of decode ways at each index
        # this is the base case where if our step reach beyond the len of s
        # then it return 1 (way of decoding)
        # also edge case for empty s
        self.dp = {len(s): 1}

        # start at index 0
        result = self.dfs(0, s)
        return result

class NeetSolution:
    """
    DP approach

    time complexity O(n)
    space complexity O(1)
    """
    def numDecodings(self, s: str) -> int:
        # edge case for empty s
        # also base case for dp
        dp = {len(s): 1}
        # loop backwards -> start from last char
        for i in range(len(s) - 1, -1, -1):
            # if char is 0, then it is not possible to decode
            if s[i] == "0":
                dp[i] = 0
            # if curr char is 1->9, then it is possible to decode
            # we put the previous solved index (i+1 since we are going backwards) into the current index first
            else:
                dp[i] = dp[i + 1]
            # same condition as the recursive approach
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                # same pos we add on the previous solved index (i+2 since we are going backwards)
                dp[i] += dp[i + 2]
        return dp[0]