from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1 = {}
        n2 = {}

        for idx, val in nums1:
            n1[idx] = val
        for idx, val in nums2:
            n2[idx] = val

        max_id = max(nums1[-1][0], nums2[-1][0])
        ans = []

        for i in range(1, max_id + 1):
            if i in n1 and i in n2:
                ans.append([i, n1[i] + n2[i]])
            elif i in n1:
                ans.append([i, n1[i]])
            elif i in n2:
                ans.append([i, n2[i]])
            else:
                continue
        
        return ans


class NeetSolution:
    """
    similiar to merge sort

    time complexity: O(n + m)
    space complexity: O(1)
    """
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                ans.append(nums1[i])
                i += 1
            elif nums2[j][0] < nums1[i][0]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
        
        while i < len(nums1):
            ans.append(nums1[i])
            i += 1

        while j < len(nums2):
            ans.append(nums2[j])
            j += 1

        return ans