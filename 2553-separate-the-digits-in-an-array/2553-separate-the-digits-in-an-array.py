class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res += list(str(num))

        for i in range(len(res)):
            res[i] = int(res[i])

        return res