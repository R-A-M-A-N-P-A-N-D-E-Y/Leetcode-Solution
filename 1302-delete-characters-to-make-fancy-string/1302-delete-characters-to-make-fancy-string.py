class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for i in range(2, len(s)):
            if s[i - 2] == s[i - 1] == s[i]:
                pass
            else:
                res += s[i - 2]
        
        res += s[-2:]
        return res