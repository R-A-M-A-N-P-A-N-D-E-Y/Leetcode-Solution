class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = max(nums)
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] < nums[i + 1]:
                temp = nums[i]
                while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                    temp += nums[i + 1]
                    i += 1
                ans = max(ans, temp)
            else:
                i += 1
        
        return ans