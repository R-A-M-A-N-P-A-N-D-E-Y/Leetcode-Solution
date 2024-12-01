class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        mp={}

        for i in range(len(nums)):
            if nums[i]*2 in mp or nums[i]/2 in mp:
                return True
                

            else:
                mp[nums[i]]=1+mp.get(nums[i],0)
        return False