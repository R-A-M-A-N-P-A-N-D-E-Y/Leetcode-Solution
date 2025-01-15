class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        s1 = bin(num1).count("1")
        s2 = bin(num2).count("1")

        if s1 - s2 > 0:
            temp = num1
            for i in range(s1 - s2):
                temp = temp & (temp - 1)
            return temp 
        elif s1 - s2 < 0:
            temp = num1
            for i in range(s2 - s1):
                temp = temp | (temp + 1)
            return temp 
        else:
            return num1
