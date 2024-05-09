class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        hap = sorted(happiness, reverse=True)
        ans = 0

        for i in range(len(hap)):
            if k == 0 or hap[i] - i <= 0:
                return ans
            else:
                ans += hap[i] - i
                k -= 1

        return ans    