class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        n1 = len(s1)
        n2 = len(s2)

        if n1 == n2 and s1 != s2:
            return False
        elif n1 == 0 or n2 == 0:
            return True
        elif n1 == 1:
            if s1[0] == s2[0] or s1[0] == s2[-1]:
                return True
        elif n2 == 1:
            if s2[0] == s1[0] or s2[0] == s1[-1]:
                return True
        
        if n1 < n2:
            cnt = 0
            while cnt < n1 and s1[cnt] == s2[cnt]:
                cnt += 1
            if cnt == n1:
                return True
            j = -1
            while cnt < n1 and s1[j] == s2[j]:
                cnt += 1
                j -= 1
            if cnt == n1:
                return True
            return False

        if n1 > n2:
            cnt = 0
            while cnt < n2 and s1[cnt] == s2[cnt]:
                cnt += 1
            if cnt == n2:
                return True
            j = -1
            while cnt < n2 and s2[j] == s1[j]:
                cnt += 1
                j -= 1
            if cnt == n2:
                return True
            return False

        return True
        