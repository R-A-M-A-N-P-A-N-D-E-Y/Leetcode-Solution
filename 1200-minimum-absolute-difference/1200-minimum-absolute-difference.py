class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)

        temp = 10**9 + 7
        res = []
        for i in range(1, len(arr)):
            if nums[i] - nums[i - 1] < temp:
                temp = nums[i] - nums[i - 1]
                res = []
                res.append([nums[i - 1], nums[i]])
            elif nums[i] - nums[i - 1] == temp:
                res.append([nums[i - 1], nums[i]])

        return res