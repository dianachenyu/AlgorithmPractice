class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        counter = collections.Counter([word[i: i+k] for i in range(0, n, k)])
        return sum(counter.values()) - max(counter.values())
