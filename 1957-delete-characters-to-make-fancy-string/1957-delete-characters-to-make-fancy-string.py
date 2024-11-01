class Solution:
    def makeFancyString(self, s: str) -> str:
        last = False
        res = s[0]

        for c in s[1:]:
            if res[-1] == c and not last:
                last = True
                res += c
            elif res[-1] != c:
                last = False
                res += c

        return res