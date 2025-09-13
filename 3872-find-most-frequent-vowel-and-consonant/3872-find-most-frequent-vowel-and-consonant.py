class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}
        cosonents = {}

        for c in s:
            if c in 'aeiou':
                if c in vowels:
                    vowels[c] += 1
                else:
                    vowels[c] = 1
            else:
                if c in cosonents:
                    cosonents[c] += 1
                else:
                    cosonents[c] = 1

        print(max(cosonents.values()) if len(cosonents) != 0 else 0)
        v = max(vowels.values()) if len(vowels) != 0 else 0
        c = max(cosonents.values()) if len(cosonents) != 0 else 0
        return v + c