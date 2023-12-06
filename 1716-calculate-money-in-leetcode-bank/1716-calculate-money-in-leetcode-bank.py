class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        res = w * 28
        res += (7 * w * (w - 1)) // 2

        if (n % 7):
            e = n % 7
            m = w + 1
            for i in range(e):
                res += m
                m += 1

        return res
        
