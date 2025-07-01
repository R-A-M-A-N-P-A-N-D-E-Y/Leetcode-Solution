class Solution:
    def possibleStringCount(self, word: str) -> int:
        num = 1
        i = 1
        while i < len(word):
            if word[i - 1] == word[i]:
                num += 1
            i += 1

        return num