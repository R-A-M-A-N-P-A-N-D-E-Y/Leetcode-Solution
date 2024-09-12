class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            isTrue = True
            word = set(word)
            for ele in word:
                if ele not in allowed:
                    isTrue = False
            if isTrue:
                count += 1
        
        return count
                