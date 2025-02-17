from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles) # char -> available count

        def backtrack():
            ans = 0

            for c in count.keys():
                if count[c] > 0:
                    count[c] -= 1
                    ans += 1
                    ans += backtrack()
                    count[c] += 1
            return ans

        return backtrack()