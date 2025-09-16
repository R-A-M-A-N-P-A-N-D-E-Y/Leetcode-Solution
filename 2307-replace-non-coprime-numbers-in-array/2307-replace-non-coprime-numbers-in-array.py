from math import gcd, lcm
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            # keep merging until coprime
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(lcm(a, b))
        return stack
