class Solution:
    def check(self, nums: List[int]) -> bool:
        s = sorted(nums)
        if s == nums:
            return True
        
        for i in range(len(nums)):
            if s == nums[i:] + nums[:i]:
                return True
        
        return False