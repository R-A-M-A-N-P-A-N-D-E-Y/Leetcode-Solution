class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        n = len(digits)

        for i in range(n):
            ans += digits[i] * (10 ** (n - i - 1))
            # print(ans)
        ans += 1
        ans = str(ans)

        res = []
        for ele in ans:
            res.append(int(ele))
        
        return res