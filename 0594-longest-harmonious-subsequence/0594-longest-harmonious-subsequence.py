class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        
        mcount = 0
        for i in count.keys():
            if i+1 in count:
                if count[i] + count[i+1] > mcount:
                    mcount = count[i] + count[i+1]
        
        return mcount