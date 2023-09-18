class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        n, m, ans = len(A), len(A[0]), 0
        H, V = [row[:] for row in A], [row[:] for row in A]
        for i in range(n):
            for j in range(m):
                if i and H[i][j]: H[i][j] += H[i - 1][j]
                if j and V[i][j]: V[i][j] += V[i][j - 1]
        for i in range(n):
            for j in range(m):
                for k in range(min(H[i][j], V[i][j]), ans, -1):
                    if V[i - k + 1][j] >= k and H[i][j - k + 1] >= k:
                        ans = k
                        break
        return ans * ans