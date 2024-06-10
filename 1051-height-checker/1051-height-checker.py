class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        res = 0
        n = len(heights)

        for i in range(n):
            if heights[i] != sorted_height[i]:
                res += 1

        return res