from typing import List
from math import sqrt

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Sieve of Eratosthenes
        primes = [True]*1001 # 1 extra for the last j + 1 in the while loop
        primes[0], primes[1] = False, False
        for i in range(2, 1001):
            if primes[i]:
                j = i*i
                while j <= 1000:
                    primes[j] = False
                    j += i
        
        for i in range(len(nums)):
            if i == 0:
                for j in range(1, nums[i]):
                    if primes[nums[i] - j]:
                        nums[i] = j
                        break
            else:
                for j in range(nums[i-1]+1, nums[i]):
                    if primes[nums[i] - j]:
                        nums[i] = j
                        break

        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False

        return True
    

class NeetSolution:
    """
    greedy solution

    time complexity: O(n*sqrt(n)*m) where m is the number of primes
    """
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n < 2:
                return False
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True

        prev = 0

        for n in nums:
            upper_bound = n - prev # non inclusive

            largest_p = 0
            for i in reversed(range(2, upper_bound)):
                if is_prime(i):
                    largest_p = i
                    break
                
            if n - largest_p <= prev:
                return False
                
            prev = n - largest_p

        return True
    

class NeetSolution:
    """
    time complexity: O(n+m*sqrt(n))
    """
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n < 2:
                return False
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True

        primes = [0, 0] # primes[i] => largest prime <= i
        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i-1])

        prev = 0

        for n in nums:
            upper_bound = n - prev # non inclusive

            largest_p = primes[upper_bound - 1]
                
            if n - largest_p <= prev:
                return False
                
            prev = n - largest_p

        return True