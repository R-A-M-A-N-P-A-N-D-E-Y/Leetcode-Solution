class Solution:
    def firstUniqChar(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in stack:
                return i
            stack.append(s[i])
        return -1