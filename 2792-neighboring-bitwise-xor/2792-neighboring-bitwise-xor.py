class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = derived[0]

        for a in derived[1:]:
            ans ^= a
        
        return True if ans == 0 else False