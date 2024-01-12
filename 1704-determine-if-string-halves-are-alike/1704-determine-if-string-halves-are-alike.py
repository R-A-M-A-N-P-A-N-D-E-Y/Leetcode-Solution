class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        half = len(s) // 2
        a = s[0:half]
        b = s[half:len(s)]
        count = 0
        c = 0
        for i in a:
            if i in 'aeiouAEIOU':
                count+=1
        for j in b:
            if j in 'aeiouAEIOU':
                c+=1
        if c == count:
            return True
        else:
            return False