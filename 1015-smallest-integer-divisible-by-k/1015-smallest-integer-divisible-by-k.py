class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        elif k % 5 == 0:
            return -1
        else:
            num = 1
            i = 1
            while num % k != 0:
                num = num * 10 + 1
                i += 1
            
            return i