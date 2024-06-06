class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Frequency map using Counter
        count = Counter(hand)

        # Sorted keys
        sorted_keys = sorted(count.keys())

        for key in sorted_keys:
            if count[key] > 0:
                for i in range(1, groupSize):
                    if count[key + i] < count[key]:
                        return False
                    count[key + i] -= count[key]
        return True