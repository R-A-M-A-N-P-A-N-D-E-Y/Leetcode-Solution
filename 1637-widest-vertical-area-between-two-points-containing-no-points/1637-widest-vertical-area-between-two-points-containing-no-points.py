class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ls = sorted(points, key=lambda x: x[0])

        m = -1
        for i in range(len(ls)-1):
            if m < ls[i+1][0] - ls[i][0]:
                m = ls[i+1][0] - ls[i][0]

        return m