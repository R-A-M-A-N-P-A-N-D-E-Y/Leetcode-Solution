class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1 = bin(num1)[2:]
        n2 = bin(num2)[2:]

        b1 = [int(bit) for bit in n1]
        b2 = [int(bit) for bit in n2]

        s1 = sum(b1)
        s2 = sum(b2)

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
