from typing import List
from collections import defaultdict

class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        total = 0
        for n in nums:
            count[n] += 1
            total += 1
        ans = []
        for num, cnt in count.items():
            if cnt > total/3:
                ans.append(num)

        return ans
    
class Solution:
    """
    Boyer-Moore Voting Algorithm

    time complexity: O(n)
    space complexity: O(1)
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count

        ans = []
        for n in count:
            if nums.count(n) > len(nums)//3:
                ans.append(n)
        return ans