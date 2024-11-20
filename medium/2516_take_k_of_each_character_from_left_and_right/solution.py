class NeetSolution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        sliding window

        time complexity: O(n)
        space complexity: O(1)
        """
        # calc total count
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord("a")] += 1

        if min(count) < k:
            return -1

        # sliding window to find the central part
        # maximize the window while make sure the window outside satisfis the k condition
        ans = float("inf")
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord("a")] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord("a")] += 1
                l += 1

            ans = min(ans, len(s) - (r - l + 1))

        return ans