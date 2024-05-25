class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_index = dict()
        
    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False
        self.nums.append(val)
        self.val_index[val] = len(self.nums) - 1
        return True       

    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        i = self.val_index[val]
        val2 = self.nums[-1]
        self.nums[i], self.nums[-1] = self.nums[-1], self.nums[i]
        self.nums.pop()
        self.val_index[val2] = i
        del self.val_index[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.nums)

  
