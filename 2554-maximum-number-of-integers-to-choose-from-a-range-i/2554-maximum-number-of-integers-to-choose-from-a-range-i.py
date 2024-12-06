class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cnt, total = 0, 0
        banned = set(banned)
        for i in range(1, n+1):
            if i in banned:
                pass
            elif i + total <= maxSum:
                cnt += 1
                total += i
            else:
                break
        
        return cnt