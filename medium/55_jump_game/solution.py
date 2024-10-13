from typing import List

class Solution:
    """
    DP bottom up with memoization

    from the back the list, we check if we can reach the end from the current index OR there is a step within the jump range that can reach the end.
    """
    def check_step(self, idx, jumps):
        """
        given an index, check if there is a step within the jump range that can reach the end from the cache
        """
        for jump in range(0, jumps+1):
            if idx+jump in self.dp:
                if self.dp[idx+jump]:
                    return self.dp[idx+jump]
        return False

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        # key: index
        # value: can reach end or not from this index
        self.dp = {}
        self.nums = nums
        # ignore the last element, since we are already there
        for i in range(len(self.nums)-2, -1, -1):
            # either we can reach the end from this index or there is a step within the jump range that can reach the end
            if (i + self.nums[i] >= len(self.nums) - 1) or self.check_step(i, self.nums[i]):
                self.dp[i] = True
            else:
                self.dp[i] = False

        return self.dp[0]