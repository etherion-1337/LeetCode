from typing import List

class Solution:
    """
    two pointers

    time complexity: O(n log n) due to sorting
    space complexity: O(1)
    """
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        print(people)
        l, r = 0, len(people) - 1
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                ans += 1
            else:
                r -= 1
                ans += 1
        
        if l == r:
            ans += 1

        return ans

class Solution:
    """
    Neetcode solution
    two pointers with sorting
    """
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]: # need to check l <= r again due to the decrement of r
                l += 1
        return res