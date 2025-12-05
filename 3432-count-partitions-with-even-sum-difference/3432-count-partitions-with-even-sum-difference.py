class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        temp = 0
        ans = 0

        for i in range(len(nums) - 1):
            temp += nums[i]
            total -= nums[i]
            if (temp - total) % 2 == 0:
                ans += 1
        
        return ans