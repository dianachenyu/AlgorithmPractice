# Method 1: Reservoir Sampling
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def pick(self, target: int) -> int:
        res = -1
        count = 0
        for idx, num in enumerate(self.nums):
            if num == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = idx
        return res


# Method 2 
class Solution:
    def __init__(self, nums: List[int]):
        self.storage = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            self.storage[num].append(idx)

    def pick(self, target: int) -> int:
        idxs = self.storage[target]
        idx = random.randint(0, len(idxs) - 1)
        return idxs[idx]
