class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counts_are_same = Counter(s1) == Counter(s2)
        diffs_are_few = sum(c1 != c2 for c1, c2 in zip(s1, s2)) <= 2

        return counts_are_same and diffs_are_few