from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p,s) for p,s in zip(position, speed)]
        pos_speed.sort(reverse = True)

        stack = []
        for p, s in pos_speed:
            hr = (target - p)/s
            if not stack:
                stack.append(hr)
            if stack and hr > stack[-1]:
                stack.append(hr)
        
        return len(stack)