class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = word.find(ch)
        return word[0:x+1][::-1] + word[x+1:]