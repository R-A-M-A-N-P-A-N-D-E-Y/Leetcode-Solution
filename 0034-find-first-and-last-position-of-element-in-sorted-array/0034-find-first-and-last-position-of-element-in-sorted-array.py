class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            count = []
            x = nums.index(target)
            count.append(x)
            while(x+1 < len(nums) and nums[x+1] == target):
                x += 1
            count.append(x)
            
            return count