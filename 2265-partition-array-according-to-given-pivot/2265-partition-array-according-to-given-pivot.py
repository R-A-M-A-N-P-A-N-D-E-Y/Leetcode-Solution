class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre = []
        mid = []
        post = []

        for ele in nums:
            if ele < pivot:
                pre.append(ele)
            elif ele > pivot:
                post.append(ele)
            else:
                mid.append(ele)
        
        return pre + mid + post