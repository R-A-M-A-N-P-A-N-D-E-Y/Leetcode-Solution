class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        binary = ""
        for i in range(len(nums)):
            binary += str(nums[i]) 
            # print("binary", binary)
            num = int(binary, 2)
            # print("num", str(num)[-1])
            if (num % 10) == 0 or (num % 10) == 5:
                res.append(True)
            else:
                res.append(False)
        
        return res