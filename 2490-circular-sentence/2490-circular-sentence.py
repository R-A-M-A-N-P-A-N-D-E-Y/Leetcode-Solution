class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        if len(words) < 2:
            return words[0][0] == words[0][-1]
        c = words[0][0]
        for word in words:
            if c == word[0]:
                c = word[-1]
            else:
                return False
        
        return words[0][0] == words[-1][-1]