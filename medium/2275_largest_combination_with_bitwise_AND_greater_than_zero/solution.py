from typing import List

class Solution:
    """
    for each number, we will count the number of 1s in its binary representation
    we just need to find the maximum number of 1s in the binary representation of the numbers
    because the numbers with 1s at those position will have the maximum bitwise AND that is greater than 0

    time complexity: O(n)
    space complexity: O(1)
    """
    def largestCombination(self, candidates: List[int]) -> int:
        # 32bit int
        bit_arr = [0]*32

        for n in candidates:
            i = 0
            while n > 0:
                bit_arr[i] += 1 & n
                i += 1
                n = n >> 1

        return max(bit_arr)
    
class NeetSolution:
    """
    space optimized solution
    """
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0

            for n in candidates:
                if (1 << i) & n:
                    count += 1

            ans = max(ans, count)

        return ans