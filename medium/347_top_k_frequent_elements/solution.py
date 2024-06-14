from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        sorted_key = sorted(hash_map, key=hash_map.get, reverse=True)
        return sorted_key[:k]
    
    
    
