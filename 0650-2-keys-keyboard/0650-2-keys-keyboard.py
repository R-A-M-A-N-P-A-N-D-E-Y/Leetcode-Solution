class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        
        while n % 2 == 0:
            ans += 2
            n //= 2
        
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                ans += i
                n //= i
        
        if n > 2:
            ans += n
        
        return ans