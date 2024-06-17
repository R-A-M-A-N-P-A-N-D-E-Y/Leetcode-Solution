class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        z = int(sqrt(c))
        i = 0
        while i <= z:
            s = i**2 + z**2
            if s == c:
                return True
            elif s > c:
                z -= 1
            else:
                i += 1
        
        return False
