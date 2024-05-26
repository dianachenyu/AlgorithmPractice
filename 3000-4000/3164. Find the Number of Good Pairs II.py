class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        counter = collections.Counter(num*k for num in nums2)
        c = [0] * (max(nums1) + 1)

        for num2, count in counter.items():
            for multiplier in range(num2, len(c), num2):
                c[multiplier] += count
        return sum(c[num1] for num1 in nums1)


# Time O(mlogm), m=max(nums1), n=len(nums2)
# Space O(m+n)
# solution:
# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/solutions/5209378/o-nlogn-beats-100-full-explanation/
