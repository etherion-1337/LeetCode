class Solution:
    def numberOfSteps (self, num: int) -> int:
        return self.subroutine(num, 0)

    def subroutine(self, num, step):
        if num == 0:
            return step

        if num%2 == 0:
            num /= 2
        else:
            num -= 1
        step += 1

        return self.subroutine(num, step)


if __name__ == "__main__":
    soln = Solution()
    ans = soln.numberOfSteps(8)
    print(ans)