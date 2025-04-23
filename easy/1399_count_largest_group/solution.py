class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_dict = {}

        for i in range(1, n + 1):
            digit_sum = sum([int(d) for d in list(str(i))])
            if digit_sum in sum_dict:
                sum_dict[digit_sum].append(i)
            else:
                sum_dict[digit_sum] = [i]
        
        size = 0
        for k, v in sum_dict.items():
            size = max(size, len(v))
        ans = 0
        for k, v in sum_dict.items():
            if len(v) == size:
                ans += 1
        return ans