from typing import List

class Solution:
    """
    DP solution

    check if any of the subarray sum is equal to the half of the total sum -> target sum, which means the rest of the array is also equal to target sum
    DP from the end of the array (bottom up DP)
    we maintan a list of all possible sum of subarray at index i (which means all possible sum value in sub array nums[i:])
    in each iteration, we
    1. add the current element to the dp list, since this num alone can be a valid sum by itself
    2. retain the previous sum value in dp list since they are still valid sum value (from the previous subarray)
    3. add the current element to the previous sum value in dp list (except the last value which is the curr value), since the sum of the previous subarray + the current element can be a valid sum value

    if the target is in the dp list, return True, otherwise return False

    time complexity: O(2^n), n is the length of the nums
    """
    def canPartition(self, nums: List[int]) -> bool:
        dp = []
        # if total sum is odd then it is impossible to partition the array into two equal sum subarray, since all elements are int
        if sum(nums)%2: # odd
            return False
        else:
            target = sum(nums)//2
        
        for i in range(len(nums)-1, -1, -1):
            # add the current element to the dp list
            dp.append(nums[i])
            # retain the previous sum value in dp list
            # add curr to all previous sum value in dp list, except the last value since it is the curr value
            for j in range(len(dp)-1):
                dp.append(dp[j] + nums[i])
            if target in dp:
                return True
            # deduplicate the dp list since we can have duplicate in nums, we just need unique possible/valid sum value
            # without this we will have memory error on LC
            dp = list(set(dp))

        return False
    

class NeetSolution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        # NeetCode used a set with initial value 0
        # so subsequent if curr num + all existing value in set will have a curr value (0 + curr = curr)
        # so no need to append curr and also when adding curr to all existing value in set, we don't need to code to avoid last value
        dp = set() 
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            # we cannot update dp while iterating over it, so we need to create a new set
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                # this is just to prevseve whatever value we have in dp into the nextDP
                # you could also clone it first
                nextDP.add(t)
            dp = nextDP
        return False
