class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        delete_cnt = 0
        # accumulate delete count along the way, if met with a char we will deplete one, if fully depleted we will add the char
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                delete_cnt += 1
            elif delete_cnt:
                delete_cnt -= 1
            else:
                ans.append(s[i])

        return "".join(ans[::-1])