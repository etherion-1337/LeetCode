from typing import List

class Solution:
    """
    Greedy approach: choose the smallest number first

    Time complexity: O(n)
    space complexity: O(n)

    key step is to store the banned numbers in a set for O(1) lookup
    else will TLE    
    """
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        curr_sum = 0
        ans = []
        banned = set(banned)
        for num in range(1, n + 1):
            if num not in banned and curr_sum + num <= maxSum:
                ans.append(num)
                curr_sum += num
            if curr_sum + num > maxSum:
                break

        return len(ans)