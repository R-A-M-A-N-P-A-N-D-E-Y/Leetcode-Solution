class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        i, j = 0, 1
        while j < len(nums):
            if nums[i] < nums[j]:
                temp = 1
                while j < len(nums) and nums[i] < nums[j]:
                    i += 1
                    j += 1
                    temp += 1
                if temp > res:
                    res = temp
            elif nums[i] > nums[j]:
                temp = 1
                while j < len(nums) and nums[i] > nums[j]:
                    i += 1
                    j += 1
                    temp += 1
                if temp > res:
                    res = temp
            else:
                i += 1
                j += 1
        
        return res