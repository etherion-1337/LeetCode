from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        time complexity: O(n) where n is the total number of bricks in the wall
        space complexity: O(n) where n is the total number of bricks in the wall
        """
        # count the number of cut point
        count = {}
        # the max limit of the cut point, we cannot use this point to cut the wall
        max_limit = sum(wall[0])
        
        for row in wall:
            tmp = 0
            # for each row in the wall, we calculate the cut point
            for i in range(0, len(row)):
                tmp += row[i]
                if tmp == max_limit:
                    continue
                if tmp not in count:
                    count[tmp] = 1
                else:
                    count[tmp] += 1

        # edge case of [[1], [1], [1]]
        if not count:
            return len(wall)
        # find the cut point that has the most count
        cut_count = count[max(count, key=count.get)]
        # the number of bricks that we need to cut
        ans = len(wall) - cut_count

        return ans
    
class NeetSolution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = { 0 : 0 }    # { Position : Gap count }

        for r in wall:
            total = 0   # Position
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())    # Total number of rows - Max gap