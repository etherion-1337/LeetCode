from typing import List
from math import sqrt

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(time):
            total_cars = 0
            for r in ranks:
                total_cars += int(sqrt(time/r))
            return total_cars >= cars

        l, r = 1, max(ranks) * (cars**2)
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if can_repair(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans