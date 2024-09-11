class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = binary(start)
        g = binary(goal)

        if len(s) != len(g):
            if len(s) > len(g):
                g = '0' * (len(s) - len(g)) + g
            else:
                s = '0' * (len(g) - len(s)) + s
        
        ans = 0
        for i in range(len(s)):
            if s[i] != g[i]:
                ans += 1
        
        return ans

def binary(num: int) -> str:
    ans = ''
    while num > 0:
        ans += str(num % 2)
        num = (num) // 2
    
    return ans[::-1]