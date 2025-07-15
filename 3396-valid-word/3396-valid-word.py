class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        # hasdigit = any(char.isdigit() for char in word)
        # hasletter = any(c.isalpha() for c in word)

        # if not hasdigit or not hasletter:
        #     return False
        for ele in word:
            if ele in '[@_!#$%^&*()<>?/\|}{~:]':
                return False
                
        vowel = ['a', 'e', 'i', 'o', 'u']
        consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

        hasvowel = False
        hasconsonant = False
        for ele in word:
            if ele.lower() in vowel:
                hasvowel = True
            elif ele.lower() in consonant:
                hasconsonant = True
        
        if hasvowel and hasconsonant:
            return True
        else:
            return False