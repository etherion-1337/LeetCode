from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                l,  r = j + 1, len(nums) - 1

                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum > target:
                        r -= 1
                    elif four_sum < target:
                        l += 1
                    else:
                        ans.add(tuple([nums[i], nums[j], nums[l], nums[r]]))
                        l += 1

        return list(ans)
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res