class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        x, y = 0, 0
        temp = 10**9
        ans = 0

        while nums != sorted(nums):
            for i in range(1, len(nums)):
                if nums[i-1] + nums[i] < temp:
                    x, y = i-1, i
                    temp = nums[i - 1] + nums[i]
            del nums[y]
            nums[x] = temp
            temp = 10**9
            ans += 1

        return ans