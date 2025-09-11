class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        ch = []
        s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                ch.append(ord(s[i]))
                s[i] = '_'
        
        if '_' in s:
            ch.sort()
            j = 0
            for i in range(len(s)):
                if s[i] == '_':
                    s[i] = chr(ch[j])
                    j += 1
            
        return ''.join(s)
        