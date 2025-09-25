class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        if len(triangle) == 2:
            return min((triangle[0][0] + triangle[1][0]), (triangle[0][0] + triangle[1][1]))
        
        else:
            i = 1
            while i < len(triangle):
                for j in range(len(triangle[i])):
                    if j == 0:
                        triangle[i][j] += triangle[i - 1][0]
                    elif j == len(triangle[i]) - 1:
                        triangle[i][j] += triangle[i - 1][-1]
                    else:
                        triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i-1][j])
                i += 1
        # print(triangle)
        return min(triangle[-1])