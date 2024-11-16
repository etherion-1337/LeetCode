from typing import List

class Solution:
    """
    sliding window brute force solution

    time complexity: O(n*k)
    space complexity: O(k)
    """
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # get all subarrays of size k
        for i in range(len(nums) - k + 1):
            sub_arr = nums[i:i+k]
            valid = True
            # check if subarray is valid
            for j in range(len(sub_arr) - 1):
                if sub_arr[j] != (sub_arr[j+1] - 1):
                    valid = False
            if valid:
                ans.append(sub_arr[-1])
            else:
                ans.append(-1)

        return ans
    
class NeetSolution:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = 0
        consec_count = 1 # lowest will 1, think of it as the smallest possible sub arr size
        for r in range(len(nums)):
            # consec streak, added r > 0 to avoid r - 1 out of bound
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                consec_count += 1
            
            if r - l + 1 > k:
                # if the window go forward and the left part is part of consec streak
                # need to remove it
                if nums[l] + 1 == nums[l + 1]:
                    consec_count -= 1
                l += 1 # move the window
            
            # check if the window is valid
            if r - l + 1 == k:
                if consec_count == k:
                    ans.append(nums[r])
                else:
                    ans.append(-1)

        return ans