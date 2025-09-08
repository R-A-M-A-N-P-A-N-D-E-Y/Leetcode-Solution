class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n - 1

        while a < n and b > 0:
            if '0' in list(str(a)) or '0' in list(str(b)):
                a += 1
                b -= 1
                continue
            else:
                if a + b == n:
                    return [a, b]
            a += 1
            b -= 1