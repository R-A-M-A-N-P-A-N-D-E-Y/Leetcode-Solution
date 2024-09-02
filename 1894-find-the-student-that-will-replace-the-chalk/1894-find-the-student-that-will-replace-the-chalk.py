class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        time = k // s
        k -= (time * s)

        for i, value in enumerate(chalk):
            k -= value
            if k < 0:
                return i

        return -1