from typing import List

class Solution:
    """
    cheesy solution with merge and sort
    time complexity: O((m+n)log(m+n))
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums)%2 == 0:
            mid_1 = int(len(nums)//2)
            mid_2 = int(len(nums)//2) + 1
            return (nums[mid_1-1] + nums[mid_2-1])/2
        else:
            mid = int(len(nums)//2) + 1
            return nums[mid-1]
        

class NeetSolution:
    """
    time complexity: O(log(m+n))
    run binary search on the shorter list
    deduce the required index of the cut off point in the longer list
    check if the cut off point is valid by comparing the left and right partition of the two lists
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total//2

        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        # for binary search in A only
        l, r = 0, len(A) - 1
        while True:
            # index of midpt in A
            i = (l + r) // 2
            # index of the cut off point in B
            j = half - (i + 1) - 1

            # edge case of out-of-bound index
            # esp the while loop is set to True instead of the usual L <= R for binary search
            # if A is an empty list, or we have search too left on A
            Aleft = A[i] if i >= 0 else float("-infinity")
            # if we want to include all elements in A in the final left partition -> searched too right
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            # same as A
            Bleft = B[j] if j >= 0 else float("-infinity")
            # same as A
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # the partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # need to reduce the partition in A
            elif Aleft > Bright:
                r = i - 1
            # need to increase the partition in A such that the partition in B is reduced
            else:
                l = i + 1