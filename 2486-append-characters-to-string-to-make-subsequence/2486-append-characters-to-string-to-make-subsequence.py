class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for k in range(len(s)):
            if j < len(t) and s[k] == t[j]:
                j += 1
        return len(t) - j