class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        for ind in range(n-1, -1, -1):
            l = 0
            maxi = maxAns = -1
            for j in range(ind, min(ind+k, n)):
                l += 1
                maxi = max(maxi, arr[j])
                TotalSum = l * maxi + dp[j+1]
                maxAns = max(maxAns, TotalSum)
            dp[ind] = maxAns
        
        return dp[0]
