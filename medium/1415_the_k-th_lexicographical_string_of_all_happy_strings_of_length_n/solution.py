class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2**(n-1))

        ans = []
        choices = "abc"
        left, right = 1, total_happy

        for i in range(n):
            curr = left
            partition_size = (right - left + 1) // len(choices)
            # polling: 1 - 4, 5 - 8, 9 - 12

            for c in choices:
                # cur <= k < cur + partition_size
                if k in range(curr, curr + partition_size):
                    ans.append(c)
                    left = curr
                    right = curr + partition_size - 1
                    choices = "abc".replace(c, "")
                    break

                curr += partition_size
        
        return "".join(ans)