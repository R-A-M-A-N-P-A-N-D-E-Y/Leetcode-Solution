from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []
        for spell in spells:
            # Minimum potion value needed to reach 'success'
            required = (success + spell - 1) // spell  # ceil(success / spell)
            # Find the first potion >= required
            index = bisect_left(potions, required)
            ans.append(m - index)
        return ans