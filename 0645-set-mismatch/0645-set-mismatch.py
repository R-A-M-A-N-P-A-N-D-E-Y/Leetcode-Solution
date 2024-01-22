class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Calculate the expected sum of 1 to n
        expected_sum = n * (n + 1) // 2

        # Use a set to identify the duplicate
        seen = set()
        duplicate = 0
        actual_sum = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            actual_sum += num

        # Calculate the missing number
        missing = expected_sum - actual_sum + duplicate

        return [duplicate, missing]