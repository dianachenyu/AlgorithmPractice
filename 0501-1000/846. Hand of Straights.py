class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = collections.Counter(hand)
        for num in sorted(counter.keys()):
            if counter[num] > 0:
                count = counter[num]
                for num in range(num, num + groupSize):
                    counter[num] -= count
                    if counter[num] < 0:
                        return False
        return True

