class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if searchWord in sentence:
            sentence = sentence.split()
            for i, word in enumerate(sentence):
                if searchWord in word and searchWord == word[:len(searchWord)]:
                    return i+1
            return -1
        else:
            return -1