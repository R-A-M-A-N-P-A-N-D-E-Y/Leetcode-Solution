class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0

        skill.sort()
        n = len(skill)
        res = skill[0] + skill[-1]
        ans += skill[0] * skill[-1]

        for i in range(1, n//2): 
            if skill[i] + skill[n - i - 1] == res:
                ans += skill[i] * skill[n - i - 1]
            else:
                return -1
        
        return ans