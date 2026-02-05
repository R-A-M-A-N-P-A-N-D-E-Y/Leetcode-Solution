class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                if i + nums[i] > n - 1:
                    res.append(nums[(nums[i] + i) % n])
                else:
                    res.append(nums[i + nums[i]])
            elif nums[i] < 0:
                if abs(nums[i]) > i:
                    res.append(nums[-1 * ((abs(nums[i]) - i) % n)])
                else:
                    res.append(nums[i - abs(nums[i])])
            else:
                res.append(nums[i])
        
        return res