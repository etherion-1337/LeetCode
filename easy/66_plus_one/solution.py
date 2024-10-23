from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp_int = int("".join([str(n) for n in digits]))
        tmp_int += 1
        result = [int(char) for char in str(tmp_int)]

        return result
    
class NeetSolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        # reverse the arr for easier calculation
        digits = digits[::-1]
        carry = True
        i = 0

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = False
            else:
                digits.append(1)
                carry = False
            i += 1

        return digits[::-1]