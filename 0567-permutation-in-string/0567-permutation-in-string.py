class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s = list(s1)
        s.sort()
        l = len(s1)

        for i in range(len(s2)):
            ss = list(s2[i:l+i])
            ss.sort()
            if s == ss:
                return True
        
        return False