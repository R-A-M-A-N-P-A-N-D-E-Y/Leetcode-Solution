class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for val, cnt in count.items():
            if cnt == n:
                return val