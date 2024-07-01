from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Sort the cars by their position in descending order.
        if the car in front is slower than the car behind, the car behind will catch up to the car in front.
        they will then merge into a single fleet
        for each car, we check if it will merge with the car in front of it
        and we keep only the one since faster one will be merged into the slower one

        time complexity: O(nlogn) due to sorting
        space complexity: O(n) for storing the position and speed of the cars
        """
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
    

class NeetSolution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)