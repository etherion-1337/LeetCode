from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    BFS + Greedy

    time: O(nlogn)
    space: O(n)
    """
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_swap(nums):
            swap = 0
            num_sorted = sorted(nums)
            # original number -> idx
            nums_map = {n:i for i, n in enumerate(nums)}

            for i in range(len(nums)):
                if nums[i] != num_sorted[i]:
                    swap += 1
                    j = nums_map[num_sorted[i]]
                    nums[i], nums[j] = nums[j], nums[i]
                    nums_map[nums[i]] = i
                    nums_map[nums[j]] = j

            return swap

        # bfs
        q = deque([root])
        ans = 0
        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans += count_swap(level)

        return ans