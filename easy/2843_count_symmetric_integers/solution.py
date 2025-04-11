class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            digit_list = [int(n) for n in list(str(i))]
            if not len(digit_list) % 2:
                half_length = len(digit_list) // 2
                if sum(digit_list[:half_length]) == sum(digit_list[half_length:]):
                    ans += 1

        return ans