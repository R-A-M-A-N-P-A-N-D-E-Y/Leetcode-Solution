class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        ls = list(s)
        
        for ele in ls:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1
        l = dict(sorted(dic.items(), key=lambda item: (-item[1], item[0])))
        res = ''
        for k, v in l.items():
            res += k*v
        
        return res