class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1][0]:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        res = [char * count for char, count in stack]
        return ''.join(res)
