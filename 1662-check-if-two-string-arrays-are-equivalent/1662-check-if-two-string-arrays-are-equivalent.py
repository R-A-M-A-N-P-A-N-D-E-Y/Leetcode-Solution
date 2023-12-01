class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''.join(map(str, word1))
        str2 = ''.join(map(str, word2))

        return str1 == str2