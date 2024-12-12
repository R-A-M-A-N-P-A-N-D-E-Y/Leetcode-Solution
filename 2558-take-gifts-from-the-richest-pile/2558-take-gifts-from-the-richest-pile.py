class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for i in range(k):
            ele = max(gifts)
            ind = gifts.index(ele)
            gifts[ind] = floor(sqrt(ele))

        return sum(gifts)