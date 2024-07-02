class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = {}
        for ele in nums1:
            if ele in ls:
                ls[ele] += 1
            else:
                ls[ele] = 1
        
        res = []

        for ele in nums2:
            if ele in ls and ls[ele] != 0:
                res.append(ele)
                ls[ele] -= 1

        return res