class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            sum_left = sum(nums[:i])
            sum_right = sum(nums[i:])
            if nums[i] == 0 and sum_left == sum_right:
                res += 2
            elif nums[i] == 0 and sum_left - 1 == sum_right:
                res += 1
            elif nums[i] == 0 and sum_left == sum_right - 1:
                res += 1
        
        return res