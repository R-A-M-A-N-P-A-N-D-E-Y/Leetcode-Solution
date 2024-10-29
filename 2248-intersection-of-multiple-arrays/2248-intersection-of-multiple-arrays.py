class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l = len(nums)
        count = {}

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in count:
                    count[nums[i][j]] += 1
                else:
                    count[nums[i][j]] = 1
        
        res = []
        for key, value in count.items():
            if value == l:
                res.append(key)
        
        return sorted(res)