from typing import List
import heapq

class Solution:
    """
    Heap Sort
    time complexity: O(nlogn)
    space complexity: O(n)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        
        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)

        ans = []

        while min_heap:
            ans.append(heapq.heappop(min_heap))

        return ans
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(arr, l, r):
            """
            l, r are the pointer to the target arr
            """
            # base case
            if l == r:
                return arr
            
            # divide
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)
            # conquer
            merge(arr, l, m, r)
            return arr

        def merge(arr, l, m, r):
            left_tmp_arr = arr[l:m + 1]
            right_tmp_arr = arr[m + 1:r + 1]
            # i: pointer to the target arr, j, k: pinter to the left and right tmp arr
            i, j, k = l, 0, 0
            # choose whichever smaller from the 2 tmp arr
            while j < len(left_tmp_arr) and k < len(right_tmp_arr):
                if left_tmp_arr[j] <= right_tmp_arr[k]:
                    arr[i] = left_tmp_arr[j]
                    j += 1
                else:
                    arr[i] = right_tmp_arr[k]
                    k += 1
                i += 1
            # one of the arr will run out first, now we handle the leftover
            # only one of the left and right tmp arr will have leftover
            while j < len(left_tmp_arr):
                arr[i] = left_tmp_arr[j]
                # nums[i] = left_tmp_arr[j]
                j += 1
                i += 1
            while k < len(right_tmp_arr):
                arr[i] = right_tmp_arr[k]
                # nums[i] = right_tmp_arr[k]
                k += 1
                i += 1

        return merge_sort(nums, 0, len(nums) - 1)