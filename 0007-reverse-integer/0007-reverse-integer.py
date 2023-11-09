class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        if x > 0:
            return 0 if int(str(x)[::-1]) > MAX_INT else int(str(x)[::-1])
        else:
            x = x * -1
            return 0 if int(str(x)[::-1]) * -1 < MIN_INT else int(str(x)[::-1]) * -1