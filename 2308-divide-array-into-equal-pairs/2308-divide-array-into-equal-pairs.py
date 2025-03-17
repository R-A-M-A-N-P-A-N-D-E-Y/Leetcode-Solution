class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        i = 0
        count = 1

        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                if count % 2 != 0:
                    return False
                count = 1
                i += 1
            else:
                i += 1
                count += 1
                
        if count % 2 != 0:
            return False
        
        return True