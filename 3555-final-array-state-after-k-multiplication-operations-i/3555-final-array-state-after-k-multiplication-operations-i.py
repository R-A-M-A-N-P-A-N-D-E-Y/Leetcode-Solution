class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            ele = min(nums)
            ind = nums.index(ele)
            nums[ind] = ele * multiplier
        
        return nums