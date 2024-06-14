from collections import defaultdict
from typing import List

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        time complexity: O(n) + O(nlogn) due to sorting
        """
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        sorted_key = sorted(hash_map, key=hash_map.get, reverse=True)
        return sorted_key[:k]
    

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        time complexity: O(n) + O(n
        """
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        # freq from 0 to len(nums) which means all unique nums
        freq_list = [[] for _ in range(len(nums) + 1)]
    
        for value, count in hash_map.items():
            freq_list[count].append(value)

        # total num of value is still n, so the nested for loop below is still O(n)
        ans = []
        for i in range(len(freq_list) - 1, 0, -1):
            for j in freq_list[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
