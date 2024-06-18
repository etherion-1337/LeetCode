class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        time complexity: O(n)
        first check if the number is the leftmost number in the sequence
        if yes we check if the number+1 is in the set, if yes we increment the length
        """
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            left = num - 1
            if left not in numsSet:
                length = 1
                while (num+length) in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest