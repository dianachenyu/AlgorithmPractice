from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counter = Counter(nums)
        keys = sorted(list(counter.keys()))

        for key in keys:
            count = counter[key]
            if count > 0:
                for num in range(key, key + k):
                    if num not in counter:
                        return False
                    elif counter[num] - count < 0:
                        return False
                    else:
                        counter[num] -= count
        return True
