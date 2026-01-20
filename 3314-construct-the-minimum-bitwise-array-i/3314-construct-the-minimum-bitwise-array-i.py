class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            i = 0
            while i <= num:
                if i | (i + 1) == num:
                    ans.append(i)
                    break
                i += 1
            
            if i | (i + 1) != num:
                ans.append(-1)

        return ans