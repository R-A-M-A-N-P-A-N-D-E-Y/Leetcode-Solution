class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        m = math.ceil((math.sqrt(1 + 8 * target) - 1) / 2)
        total = m * (m + 1) / 2

        if(total - target) % 2 == 0:
            return m
        return m + 2 if m % 2 == 1 else m + 1