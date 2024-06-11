class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(arr1)):
            if arr1[i] in dic:
                dic[arr1[i]] += 1
            else:
                dic[arr1[i]] = 1
        res = []

        for i in range(len(arr2)):
            for j in range(dic[arr2[i]]):
                res.append(arr2[i])
                arr1.remove(arr2[i])

        return res + sorted(arr1)