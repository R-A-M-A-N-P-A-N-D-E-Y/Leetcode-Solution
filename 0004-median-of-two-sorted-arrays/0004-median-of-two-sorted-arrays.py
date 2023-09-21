class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        ls = []

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                ls.append(nums1[i])
                i += 1
            else:
                ls.append(nums2[j])
                j += 1
        
        while i < n:
            ls.append(nums1[i])
            i += 1
        
        while j < m:
            ls.append(nums2[j])
            j += 1
        
        n = len(ls)

        if n % 2 != 0:
            return float(ls[(n//2)])
        else:
            return float((ls[n//2]+ls[(n//2) - 1])/2)