class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        x = max(nums)
        if x>0 and x*-1 in nums:
            return x
        else:
            nums.remove(x)
            return self.findMaxK(nums)