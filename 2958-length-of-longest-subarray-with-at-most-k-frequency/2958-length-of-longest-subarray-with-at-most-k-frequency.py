class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        res = []
        i, j = 0, 1
        count = {}
        count[nums[i]] = 1
        top = 1

        while i < j and j < len(nums):
            if nums[j] in count:
                count[nums[j]] += 1
                if count[nums[j]] > top:
                    top = count[nums[j]] 
            else:
                count[nums[j]] = 1    
            
            if top > k:
                if len(nums[i:j]) > len(res):
                    res = nums[i:j]
                while top > k:
                    if count[nums[i]] == top:
                        top -= 1
                    count[nums[i]] -= 1
                    i += 1     
            
            j += 1

        return len(res) if len(res) > len(nums[i:j]) else len(nums[i:j])