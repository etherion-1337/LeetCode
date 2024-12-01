from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        check = set(arr)
        zero_counter = 0 # edge cases like [0, 0]
        ans_flag = False
        for n in arr:
            if n == 0:
                zero_counter += 1
            if n*2 in check and n != 0: # edge cases like [1, 2, 0], this should return False but if we don't check for n != 0, it will return True
                ans_flag = True
        if zero_counter > 1:
            ans_flag = True
            
        return ans_flag
    
class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def checkIfExist(self, arr: List[int]) -> bool:
        seen_num = set()
        for n in arr:
            if n*2 in seen_num or (n%2 == 0 and n/2 in seen_num):
                return True
            seen_num.add(n)

        return False