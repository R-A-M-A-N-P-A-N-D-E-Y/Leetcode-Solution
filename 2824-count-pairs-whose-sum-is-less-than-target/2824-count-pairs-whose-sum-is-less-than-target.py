class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] > target and nums[i] > 0:
                    break
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] >= target:
                    break
                res += 1
        
        return res