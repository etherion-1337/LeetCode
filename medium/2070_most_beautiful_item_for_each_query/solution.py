from typing import List
import bisect

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key = lambda x: x[0])
        hash_map = {} # k: price, v: max beauty so far
        curr_max = float("-inf")

        for item in items:
            hash_map[item[0]] = max(curr_max, item[1])
            curr_max = max(curr_max, item[1])

        key_sort = sorted(hash_map.keys())

        ans = []
        for q in queries:
            if q in hash_map:
                ans.append(hash_map[q])
            else:
                index = bisect.bisect(key_sort, q)
                next_smaller_key = key_sort[index-1] # one value smaller than q
                if next_smaller_key and next_smaller_key < q: # 2nd condition for edge case where there is only one element
                    ans.append(hash_map[next_smaller_key])
                else:
                    ans.append(0)
        return ans
    

class Solution:
    """
    brute force solution
    TLE
    """
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = []

        for q in queries:
            max_bea = 0

            for p, b in items:
                if p <= q:
                    max_bea = max(max_bea, b)

            res.append(max_bea)

        return res

class NeetSolution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort() # [p, b]
        queries = sorted([q, i] for i , q in enumerate(queries)) # [query, original index]

        ans = [0] * len(queries)
        max_beauty = 0
        j = 0 # pointer in items

        for q, i in queries:

            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            # since queries is sorted, even if the current q is not founded or smaller
            # the previous max_beauty from the previous query will be the fall back
            ans[i] = max_beauty
        
        return ans


