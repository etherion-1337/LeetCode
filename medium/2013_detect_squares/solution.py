from collections import defaultdict
from typing import List

class DetectSquares:
    """
    time complexity: O(1) for add, O(n) for count
    space complexity: O(n)
    """

    def __init__(self):
        self.point_freq = defaultdict(int)
        self.pts = []
        
    def add(self, point: List[int]) -> None:
        self.point_freq[tuple(point)] += 1
        self.pts.append(point)
        
    def count(self, point: List[int]) -> int:
        px, py = point
        ans = 0

        # look for opposite point first
        # if exist, get the 2 adj points if exist
        # the opposite point repetition is guranteed by the duplocate in the pts list
        for x, y in self.pts:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            else:
                ans += self.point_freq[x, py]*self.point_freq[px, y]

        return ans
    

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)