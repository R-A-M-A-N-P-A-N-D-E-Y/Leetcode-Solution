class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ls=[]
        for i , j in count.items():
            if j >= 2:
                ls.append(i)
        return ls