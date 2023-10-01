class Solution:
    def reverseWords(self, s: str) -> str:
        ls = []
        s = s.split(" ")
        for word in s:
            word = word[::-1]
            ls.append(word)
            
        return ' '.join(ls)