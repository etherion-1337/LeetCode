from collections import defaultdict
from typing import List

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        time complexity = O(n * mlogm) where n is the number of strings and m is the length of the longest string
        """
        hash_map = {}

        for _str in strs:
            sorted_str = "".join(sorted(_str))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [_str]
            else:
                hash_map[sorted_str].append(_str)
                
        return hash_map.values()

class NeetSolution(object):
    """
    no sorting, which typically has a time complexity of O(mlogm)
    time complexity = O(n * m * 26) -> O(n * m) where n is the number of strings and m is the length of the longest string
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            char_arr = [0] * 26
            for char in s:
                arr_ind = ord(char) - ord("a")
                char_arr[arr_ind] += 1
            
            # immutable turple as dict key
            hash_map[tuple(char_arr)].append(s)

        return hash_map.values()
    
