class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        mp = {0: -1}  # remainder -> index
        prefix = 0
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            needed = (prefix - target) % p

            if needed in mp:
                res = min(res, i - mp[needed])

            mp[prefix] = i

        return res if res < len(nums) else -1