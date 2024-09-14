class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ele = max(nums)
        pos = 0
        l = 0
        i = 0

        while i < len(nums):
            if nums[i] == ele:
                le = 1
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    le += 1
                    i += 1
                if l < le:
                    l = le
                    pos = i
            i += 1
        
        if pos == 0 and l == 0:
            return 1
        else:
            return l
