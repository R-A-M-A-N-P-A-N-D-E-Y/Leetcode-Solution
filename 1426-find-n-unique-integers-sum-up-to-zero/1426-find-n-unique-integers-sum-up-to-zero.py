class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            res = []
        else:
            res = [0]
            n -= 1
        
        i = 1
        while n > 0:
            res.append(i)
            res.append(i * -1)
            i += 1
            n -= 2
        
        return res