class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ls = list(text.split(' '))
        ch = list(brokenLetters)
        
        # print(ls[0])
        for c in ch:
            for i in range(len(ls)):
                if c in ls[i]:
                    ls[i] = '0'
        
        ls = list(filter(lambda a: a != '0', ls))
        # print('e' in 'code')
        return len(ls)