class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = cl = 0
        for c in s:
            if c == '(':
                op += 1
            elif c == ')' and op > 0:
                op -= 1
            else:
                cl += 1
        
        return op + cl