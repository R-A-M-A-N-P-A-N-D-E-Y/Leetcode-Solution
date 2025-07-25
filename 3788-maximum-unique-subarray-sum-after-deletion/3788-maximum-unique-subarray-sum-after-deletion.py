class Solution:
    def maxSum(self, nums: List[int]) -> int:
        has_positive = any(n > 0 for n in nums)
        has_negative = any(n < 0 for n in nums)

        if has_positive and has_negative:
            return sum({ele for ele in nums if ele > 0})
        elif has_positive:
            return sum({ele for ele in nums if ele > 0})
        elif has_negative:
            return max(nums)
        