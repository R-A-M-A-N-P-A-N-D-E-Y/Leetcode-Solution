class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [0] * len(score)
        for i in range(len(score)):
            temp = max(score)
            ind = score.index(temp)
            if i == 0:
                res[ind] = "Gold Medal"
                score[ind] = -1
            elif i == 1:
                res[ind] = "Silver Medal"
                score[ind] = -1
            elif i == 2:
                res[ind] = "Bronze Medal"
                score[ind] = -1
            else:
                res[ind] = str(i+1)
                score[ind] = -1
        
        return res