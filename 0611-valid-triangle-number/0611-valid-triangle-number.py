class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        # k is the largest side (num3)
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # All pairs from i...j-1 with j are valid
                    count += (j - i)
                    j -= 1
                else:
                    i += 1

        return count