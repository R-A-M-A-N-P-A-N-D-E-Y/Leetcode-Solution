class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()

        # print(s1, s2)
        ans = {}

        for word in s2:
            if word not in ans:
                ans[word] = 1
            else:
                ans[word] += 1
        
        for word in s1:
            if word not in ans:
                ans[word] = 1
            else:
                ans[word] += 1

        res = []
        for word, count in ans.items():
            if count == 1:
                res.append(word)

        return res