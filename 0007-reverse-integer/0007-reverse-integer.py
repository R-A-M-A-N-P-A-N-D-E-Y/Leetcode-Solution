class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        if x > 0:
            num = int(str(x)[::-1])
            return 0 if num > MAX_INT else num
        else:
            x = x * -1
            num = int(str(x)[::-1]) * -1
            return 0 if num < MIN_INT else num