class Solution:
    """
    time complexity: O(n)
    TLE on python but accepted on cpp

    clever tricks using OR operator: OR the current number with the target number will get a number where the set bit of the new number is the same as the target number.
    """
    def minEnd(self, n: int, x: int) -> int:
        ans = x

        for _ in range(n-1):
            ans += 1
            ans = ans | x

        return ans
    

class Solution:
    """
    time complexity: O(log2 n)

    main idea:
    we notice that we need to increase from the number x, (n-1) times to get the last number (provided we can follow all the conditions)
    essetnially the 1s in the binary representation of x cannot be touched, but we can change the 0s to 1s in the binary representation of x
    basicaly we want to interleave the binary representation of (n-1) into the 0s of the binary representation of x.
    this is because we would have to count to (n-1) to get to the last number (with those numbers fill in the 0s of x).

    n-1 because the first number is x itself, we just need to handle the rest of the numbers.
    """
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        # pointer in x
        i_x = 1
        # pointer in n
        i_n = 1

        while i_n <= n - 1:
            # if there is a 0 slot in x at this bit position
            if i_x & x == 0:
                # if the bit in n at that slot is 1, we insert it into x at that slot
                if i_n & (n - 1):
                    ans = ans | i_x
                i_n = i_n << 1

            i_x = i_x << 1

        return ans