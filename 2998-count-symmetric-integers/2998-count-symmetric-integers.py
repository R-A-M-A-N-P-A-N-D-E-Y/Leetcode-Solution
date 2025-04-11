class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if low < 11 and high > 11:
            low = 11
        count = 0
        for i in range(low, high+1):
            s = str(i)
            if len(s) % 2 == 0:
                s1, s2 = 0, 0
                for j in range(len(s) // 2):
                    s1 += int(s[j])
                    s2 += int(s[j+len(s)//2])
                if s1 == s2:
                    count += 1
        
        return count