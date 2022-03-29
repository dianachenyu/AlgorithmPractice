class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# Time: O(n)
# Space: O(1)

# Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
# thus the duplicated number will be the begin of the cycle in the linked list.
# Good explanations
# https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions%3A-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained
