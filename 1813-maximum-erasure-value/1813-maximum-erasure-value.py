class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i, j = 0, 1
        res = 0
        sol = []
        sol.append(nums[0])

        while i < len(nums):
            if nums[i] not in sol:
                sol.append(nums[i])
            else:
                if res < sum(sol):
                    res = sum(sol)
                while nums[i] in sol:
                    sol.pop(0)
                sol.append(nums[i])
            i += 1
        # print(sol)
        if res < sum(sol):
            res = sum(sol)
        return res