class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ls = set()
        for num in nums:
            if num in ls:
                return num
            ls.add(num)