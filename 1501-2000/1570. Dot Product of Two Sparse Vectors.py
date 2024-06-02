class SparseVector:
    def __init__(self, nums: List[int]):
        self.digits = dict()
        for i, num in enumerate(nums):
            if num != 0:
                self.digits[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, num in self.digits.items():
            if i in vec.digits:
                res += num * vec.digits[i]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
