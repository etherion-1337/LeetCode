from typing import List

class Solution:
    """
    time: O(nlogn)
    space: O(n)
    """
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        w_to_h_ratio = []
        for rec in rectangles:
            w_to_h_ratio.append(rec[0]/rec[1])
        w_to_h_ratio = sorted(w_to_h_ratio)

        ans = 0
        streak = 1
        prev = w_to_h_ratio[0]
        
        for i in range(1, len(w_to_h_ratio)):
            if w_to_h_ratio[i] == prev:
                streak += 1
            else:
                if streak > 1:
                    streak -= 1
                    ans += streak * (streak + 1) // 2
                prev = w_to_h_ratio[i]
                streak = 1

        if streak > 1:
            streak -= 1
            ans += streak * (streak + 1) // 2
            prev = w_to_h_ratio[i]
            streak = 0

        return ans
    

class NeetSolution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {} # w/h: count

        for w, h in rectangles:
            count[w/h] = 1 + count.get(w/h, 0)

        res = 0
        for c in count.values():
            res += (c*(c-1)) // 2

        return res