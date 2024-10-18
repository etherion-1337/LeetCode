from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Greedy solution
        time complexity: O(n)
        space complexity: O(1)

        first build a hash map to store the last index of each char in s
        then we iterate through s, for each char we update the end index of the current partition
        this is to make sure all char so far in the current partition are all included in the current partition
        """
        # key: char
        # val: last index of char appeared in s
        hash_map = {}
        for i, char in enumerate(s):
            hash_map[char] = i

        result = []
        # size of current partition
        curr_size = 0
        # the end index of current partition
        curr_end = 0
        for i, char in enumerate(s):
            curr_size += 1
            curr_end = max(curr_end, hash_map[char])

            if i == curr_end:
                result.append(curr_size)
                # no need reset curr_end since the max func will update in the start of the next partition
                curr_size = 0

        return result