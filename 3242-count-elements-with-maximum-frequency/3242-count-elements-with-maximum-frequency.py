class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        df = {}

        for i in range(len(nums)):
            if nums[i] in df:
                df[nums [i]] += 1
            else:
                df[nums[i]] = 1
        
        res = 0
        ans = 0
        for val in df.values():
            if val > res:
                ans = val
                res = val
            elif val == res:
                ans += val
        
        return ans