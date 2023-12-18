class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        n1 = min(nums)
        nums.remove(n1)
        n2 = min(nums)

        return (m1*m2) - (n1*n2)