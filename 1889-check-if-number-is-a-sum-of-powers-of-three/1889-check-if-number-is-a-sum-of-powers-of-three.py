class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        N = n

        while N > 0:
            x = N % 3

            if x == 2:
                return False

            N //= 3
            if (x < 0):
                N += 1
        
        return True