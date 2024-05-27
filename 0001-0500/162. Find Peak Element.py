class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def find(left, right):
            if left == right:
                return left
            if left + 1 == right:
                return left if nums[left] > nums[right] else right

            mid = (left + right) // 2
            if nums[mid + 1] > nums[mid]:
                return find(mid + 1, right)
            else:
                return find(left, mid)
        return find(0, n - 1)        
