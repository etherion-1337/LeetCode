class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans_list = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i == j or i == k or j == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans_list.append(tuple(sorted([nums[i],nums[j],nums[k]])))
        
        if ans_list:
            ans = [list(x) for x in list(set(ans_list))]
            return ans
        else:
            return []
        
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        time complexity: O(nlogn) + O(n^2) -> O(n^2) 
        space complexity: O(1)

        1. sort the list
        2. fix first element and use two pointer technique to find the other two elements
        3. first element if same as previous element, skip it
        4. for two pointer technique, just move left pointer again if got duplicate, the right pointer will be moved automatically based on three sum condition
        """
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans